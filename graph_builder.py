from states import TrickyQuestionGenerator
import json
from langgraph.graph import START, END, StateGraph
from ENV import OUTPUTFILE
from langchain_core.callbacks.manager import adispatch_custom_event
from langchain_core.runnables import RunnableConfig

async def generate_qa(state: TrickyQuestionGenerator):
    qa = await state["qa_generator"].generate(list_of_questions=state["list_of_questions"])
    return {"question": qa.question, "answer": qa.answer, "num_ai_answer": 0}

async def generate_answer(state: TrickyQuestionGenerator):
    ai_answer = await state["generator"].answer(state["question"])
    return {"ai_answer": ai_answer, "num_ai_answer": state["num_ai_answer"] + 1}

async def grade_answer(state: TrickyQuestionGenerator):
    if state["num_ai_answer"] >= state["max_feedback_loop"]:
        return "export_qa"
    is_correct = await state["evaluator"].aevaluate(
        answer=state["ai_answer"],
        correct_answer=state["answer"],
    )
    if is_correct:
        return "generate_question"
    return "export_qa"

async def generate_question(state: TrickyQuestionGenerator):
    rephrased = await state["discriminator"].rephrase(
        question=state["question"],
        true_answer=state["answer"],
        ai_answer=state["ai_answer"],
    )
    return {"question": rephrased}

async def export_qa(state: TrickyQuestionGenerator, config: RunnableConfig):
    for chunk in f"Exporting question after {state['num_ai_answer']} trials:\n{state['start_num_question']}. {state['question']}\nAnswer: {state['answer']}\n\n".split(" "):
        await adispatch_custom_event(
            "custom_event",
            {"chunk": chunk},
            config=config
        )

    with open(OUTPUTFILE, "r") as f:
        data = json.load(f)
    data[state["start_num_question"]] = {
        "question": state["question"],
        "answer": state["answer"],
        "ai_answer": state["ai_answer"],
    }
    with open(OUTPUTFILE, "w") as f:
        json.dump(data, f, indent=4)

    return {"start_num_question": state["start_num_question"] + 1, "list_of_questions": [state["question"]]}

def is_end(state: TrickyQuestionGenerator):
    if state["start_num_question"] > 30:
        return END
    return "generate_qa"


def build_graph():
    graph = StateGraph(TrickyQuestionGenerator)

    graph.add_node("generate_qa", generate_qa)
    graph.add_node("generate_answer", generate_answer)
    graph.add_node("generate_question", generate_question)
    graph.add_node("export_qa", export_qa)

    graph.add_edge(START, "generate_qa")
    graph.add_edge("generate_qa", "generate_answer")
    graph.add_conditional_edges("generate_answer", grade_answer, ["generate_question", "export_qa"])
    graph.add_edge("generate_question", "generate_answer")
    graph.add_conditional_edges("export_qa", is_end, ["generate_qa", END])

    builder = graph.compile()

    with open("graph.png", "wb") as f:
        f.write(builder.get_graph(xray=1).draw_mermaid_png())

    return builder

if __name__ == "__main__":
    build_graph()