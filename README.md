#AI-Powered HR Recruitment System

## Overview

This project is an end-to-end AI-powered recruitment system built using FastAPI and LangGraph. It automates resume screening, technical interviews, HR evaluation, interview scheduling, and HR chatbot queries.

---

## Architecture

User → FastAPI → LangGraph Agents → Database → Chatbot

Agents Flow:
ATS → Interview → HR → Scheduling

---

## Tech Stack

* Python
* FastAPI
* LangGraph
* SQLAlchemy
* SQLite
* WebSockets

---

## Features

### ATS Agent

* Resume parsing
* Skill matching
* Candidate scoring

### Interview Agent

* Real-time Q&A
* WebSocket communication
* Timer-based evaluation

### HR Agent

* Context-based questions
* Candidate evaluation

### Scheduling Agent

* Interview scheduling
* Email notification

### HR Chatbot

* Database-based responses
* No hallucination

---

## Memory

* Short-term → LangGraph state
* Long-term → SQLite database

---

## Setup

```bash
git clone https://github.com/shreenithyasrinivasan/hr-ai-recruitment-system.git
cd hr-ai-recruitment-system
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

---

## Demo Flow

1. Upload Resume → ATS Score
2. Start Interview
3. HR Round
4. Schedule Interview
5. Chatbot Query

---

## Note

This project demonstrates an end-to-end AI agent pipeline using LangGraph and FastAPI.
