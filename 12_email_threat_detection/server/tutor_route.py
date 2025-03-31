from fastapi import APIRouter
from tutor_service import TutorService

tutor_service = TutorService()

router = APIRouter()

@router.post("/query")
async def query(question: str):
    return tutor_service.get_question_answer(question)

@router.post("/quiz")
async def quiz(question: str, number: int):
    return tutor_service.get_quiz(question, number)

