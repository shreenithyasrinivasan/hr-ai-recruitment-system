def calculate_ats_score(resume_text: str, job_description: str):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    score = 0

    # Skill match
    skills = ["python", "sql", "machine learning", "data analysis"]
    skill_matches = sum(1 for skill in skills if skill in resume_text)
    score += (skill_matches / len(skills)) * 50

    # Keyword match
    jd_keywords = job_description.split()
    keyword_matches = sum(1 for word in jd_keywords if word in resume_text)
    score += (keyword_matches / len(jd_keywords)) * 30

    # Experience (basic check)
    if "year" in resume_text or "experience" in resume_text:
        score += 20

    return int(score)
