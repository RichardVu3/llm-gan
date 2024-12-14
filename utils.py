from ENV import OPENAI_API_KEY, OPENAI_API_BASE, MODEL, QAFile
from langchain_openai import ChatOpenAI
import json
from typing import Literal

def get_llm(*args, **kwargs) -> ChatOpenAI:
    base_url = kwargs.pop("base_url") if "base_url" in kwargs else OPENAI_API_BASE
    api_key = kwargs.pop("api_key") if "api_key" in kwargs else OPENAI_API_KEY
    model = kwargs.pop("model") if "model" in kwargs else MODEL

    return ChatOpenAI(
        base_url=base_url,
        api_key=api_key,
        model=model,
        **kwargs
    )

def format_list_of_questions(list_of_questions):
    return "\n".join([f"{i+1}. {question}" for i, question in enumerate(list_of_questions, 1)])


def parse_qa_file(to_return: Literal["question", "answer", "both"] = "both") -> list[int, str]:
    with open(QAFile, 'r') as file:
        data = json.load(file)
    if to_return == "both":
        return [(int(key), value["question"], value["answer"]) for key, value in data.items()]
    return [(int(key), value[to_return]) for key, value in data.items()]