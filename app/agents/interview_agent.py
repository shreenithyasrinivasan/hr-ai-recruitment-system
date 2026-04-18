from langgraph.graph import StateGraph
from typing import TypedDict

class InterviewState(TypedDict):
    question: str
    answer: str
    score: int


# Node 1: Generate Question
def generate_question(state: InterviewState):
    state["question"] = "What is Python and why is it used?"
    return state


# Node 2: Evaluate Answer
def evaluate_answer(state: InterviewState):
    answer = state.get("answer", "").lower()

    if "programming" in answer:
        state["score"] = 8
    else:
        state["score"] = 5

    return state


def build_interview_graph():
    builder = StateGraph(InterviewState)

    builder.add_node("generate_question", generate_question)
    builder.add_node("evaluate_answer", evaluate_answer)

    builder.set_entry_point("generate_question")
    builder.add_edge("generate_question", "evaluate_answer")

    return builder.compile()