from langgraph.graph import StateGraph
from typing import TypedDict
from app.services.ats_service import calculate_ats_score

# Define state
class ATSState(TypedDict):
    name: str
    email: str
    resume_text: str
    score: int
    stage: str


# Node 1: Calculate score
def score_resume(state: ATSState):
    job_description = "Looking for Python developer with SQL and ML skills"
    score = calculate_ats_score(state["resume_text"], job_description)

    state["score"] = score
    return state


# Node 2: Decide stage
def decide_stage(state: ATSState):
    state["stage"] = "Selected for Interview" if state["score"] >= 80 else "Rejected"
    return state


# Build graph
def build_ats_graph():
    builder = StateGraph(ATSState)

    builder.add_node("score_resume", score_resume)
    builder.add_node("decide_stage", decide_stage)

    builder.set_entry_point("score_resume")
    builder.add_edge("score_resume", "decide_stage")

    return builder.compile()
