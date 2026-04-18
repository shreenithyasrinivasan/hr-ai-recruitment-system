# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "HR AI System Running"}

# from fastapi import FastAPI
# from app.db.database import engine, Base, SessionLocal
# from app.models.candidate import Candidate
# from app.services.ats_service import calculate_ats_score

# app = FastAPI()

# Base.metadata.create_all(bind=engine)

# @app.get("/")
# def home():
#     return {"message": "HR AI System Running"}


# @app.post("/upload-resume")
# def upload_resume(name: str, email: str, resume_text: str):
#     db = SessionLocal()

#     job_description = "Looking for Python developer with SQL and ML skills"

#     score = calculate_ats_score(resume_text, job_description)

#     stage = "Selected for Interview" if score >= 80 else "Rejected"

#     candidate = Candidate(
#         name=name,
#         email=email,
#         resume_text=resume_text,
#         ats_score=score,
#         stage=stage
#     )

#     db.add(candidate)
#     db.commit()
#     db.refresh(candidate)

#     return {
#         "name": name,
#         "score": score,
#         "stage": stage
#     }
# from app.agents.ats_agent import build_ats_graph
# @app.post("/upload-resume")
# def upload_resume(name: str, email: str, resume_text: str):
#     db = SessionLocal()

#     graph = build_ats_graph()

#     result = graph.invoke({
#         "name": name,
#         "email": email,
#         "resume_text": resume_text
#     })

#     candidate = Candidate(
#         name=result["name"],
#         email=result["email"],
#         resume_text=result["resume_text"],
#         ats_score=result["score"],
#         stage=result["stage"]
#     )

#     db.add(candidate)
#     db.commit()
#     db.refresh(candidate)

#     return result

# from fastapi import FastAPI
# from app.db.database import engine, Base, SessionLocal
# from app.models.candidate import Candidate
# from app.agents.ats_agent import build_ats_graph

# app = FastAPI()   # ✅ MUST be before any @app decorators

# Base.metadata.create_all(bind=engine)

# from fastapi import FastAPI
# from app.db.database import engine, Base, SessionLocal
# from app.models.candidate import Candidate
# from app.agents.ats_agent import build_ats_graph

# # Create app FIRST
# app = FastAPI()

# # Create tables
# Base.metadata.create_all(bind=engine)


# @app.get("/")
# def home():
#     return {"message": "HR AI System Running"}


# @app.post("/upload-resume")
# def upload_resume(name: str, email: str, resume_text: str):
#     db = SessionLocal()

#     graph = build_ats_graph()

#     result = graph.invoke({
#         "name": name,
#         "email": email,
#         "resume_text": resume_text
#     })

#     candidate = Candidate(
#         name=result["name"],
#         email=result["email"],
#         resume_text=result["resume_text"],
#         ats_score=result["score"],
#         stage=result["stage"]
#     )

#     db.add(candidate)
#     db.commit()
#     db.refresh(candidate)

#     return result
# import asyncio

# @app.websocket("/ws/interview")
# async def interview(websocket: WebSocket):
#     await websocket.accept()

#     graph = build_interview_graph()

#     # Generate question
#     state = graph.invoke({})
#     question = state["question"]

#     await websocket.send_text(f"Question: {question}")

#     try:
#         # Wait for answer (30 sec timer)
#         answer = await asyncio.wait_for(websocket.receive_text(), timeout=30)
#     except asyncio.TimeoutError:
#         await websocket.send_text("Time up!")
#         await websocket.close()
#         return

#     # Evaluate answer
#     state = graph.invoke({
#         "question": question,
#         "answer": answer
#     })

#     score = state["score"]

#     await websocket.send_text(f"Score: {score}")

#     await websocket.close()
# from fastapi import FastAPI, WebSocket
# from app.db.database import engine, Base, SessionLocal
# from app.models.candidate import Candidate
# from app.agents.ats_agent import build_ats_graph
# from app.agents.interview_agent import build_interview_graph

# import asyncio

from fastapi import FastAPI, WebSocket
from app.db.database import engine, Base, SessionLocal
from app.models.candidate import Candidate
from app.agents.ats_agent import build_ats_graph
from app.agents.interview_agent import build_interview_graph

import asyncio
app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.websocket("/ws/interview")
async def interview(websocket: WebSocket):
    await websocket.accept()

    graph = build_interview_graph()

    state = graph.invoke({})
    question = state["question"]

    await websocket.send_text(f"Question: {question}")

    try:
        answer = await asyncio.wait_for(websocket.receive_text(), timeout=30)
    except asyncio.TimeoutError:
        await websocket.send_text("Time up!")
        await websocket.close()
        return

    state = graph.invoke({
        "question": question,
        "answer": answer
    })

    await websocket.send_text(f"Score: {state['score']}")
    await websocket.close()

    from app.agents.hr_agent import build_hr_graph
@app.post("/hr-round")
def hr_round(answer: str):
    graph = build_hr_graph()

    state = graph.invoke({
        "answer": answer
    })

    return {
        "question": state["question"],
        "answer": state["answer"]
    }
from app.services.email_service import send_email
@app.post("/schedule-interview")
def schedule_interview(email: str, availability: str):
    
    meeting_link = "https://meet.google.com/demo-link"

    subject = "Interview Scheduled"
    body = f"""
    Your interview is scheduled.
    
    Availability: {availability}
    Meeting Link: {meeting_link}
    """

    send_email(email, subject, body)

    return {
        "message": "Interview scheduled",
        "meeting_link": meeting_link
    }
from app.services.chatbot_service import query_candidates
@app.post("/chat")
def chat(query: str):
    response = query_candidates(query)
    return {"response": response}