from app.db.database import SessionLocal
from app.models.candidate import Candidate

def query_candidates(query: str):
    db = SessionLocal()

    if "all" in query.lower():
        candidates = db.query(Candidate).all()

    elif "selected" in query.lower():
        candidates = db.query(Candidate).filter(Candidate.stage == "Selected for Interview").all()

    elif "rejected" in query.lower():
        candidates = db.query(Candidate).filter(Candidate.stage == "Rejected").all()

    else:
        return "Sorry, I didn't understand."

    result = []
    for c in candidates:
        result.append({
            "name": c.name,
            "email": c.email,
            "score": c.ats_score,
            "stage": c.stage
        })

    return result