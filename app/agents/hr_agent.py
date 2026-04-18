from langgraph.graph import StateGraph
from typing import TypedDict

class HRState(TypedDict):
    question: str
    answer: str


# Node 1: Generate HR question
def generate_hr_question(state: HRState):
    state["question"] = "What is your notice period and when can you join?"
    return state


# Node 2: Store answer (basic)
def process_hr_answer(state: HRState):
    return state


def build_hr_graph():
    builder = StateGraph(HRState)

    builder.add_node("generate_question", generate_hr_question)
    builder.add_node("process_answer", process_hr_answer)

    builder.set_entry_point("generate_question")
    builder.add_edge("generate_question", "process_answer")

    return builder.compile()