import json
from ENV import OUTPUTFILE
from graph_builder import build_graph
from states import Evaluator, Generator, Discriminator, QuestionGenerator
import asyncio

def parse_output_file():
    with open(OUTPUTFILE, "r") as f:
        qas = json.load(f)
    start_num_question = (0 if not qas else max(map(int, qas.keys()))) + 1
    list_of_questions = [qa["question"] for qa in qas.values()]
    return start_num_question, list_of_questions

class Runner:
    def __init__(self):
        self.generator = build_graph()

    async def run(self):
        start_num_question, list_of_questions = parse_output_file()
        async for event in self.generator.astream_events(
            {
                "start_num_question": start_num_question,
                "evaluator": Evaluator(),
                "generator": Generator(),
                "discriminator": Discriminator(),
                "max_feedback_loop": 5,
                "qa_generator": QuestionGenerator(),
                "list_of_questions": list_of_questions,
            },
            {"recursion_limit": 1000},
            version="v2",
        ):
            if event["event"] == "on_custom_event" and event["name"] == "custom_event":
                data = event["data"]
                if data:
                    print(data["chunk"], end=" ", flush=True)


if __name__ == "__main__":
    runner = Runner()
    asyncio.run(runner.run())