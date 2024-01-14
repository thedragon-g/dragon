from fastapi import  HTTPException, APIRouter, Request
from app.routers.personality_test.models import Question, StartTestRequest, QuestionBatch, SubmitAnswers
from app.routers.personality_test.functions import get_first_question_batch, judge

personality_test_router = APIRouter()


@personality_test_router.post("/start-or-continue-test")
async def start_test(request: Request):
    first_batch = await get_first_question_batch((await request.json())['user_id'])
    return first_batch[0]

@personality_test_router.post("/submit-answers/")
async def submit_answers(answers: SubmitAnswers):
    # Score each answer and update the database
    scores = await judge(answers)

    return scores

