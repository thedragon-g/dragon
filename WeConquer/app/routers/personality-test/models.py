from pydantic import BaseModel, EmailStr
from typing import List, Optional


class Question(BaseModel):
    question_id: int
    question_text: str
    question_prompt: str
    trait_type: str
    sub_trait: str

class Answer(BaseModel):
    answer_id: int | None
    user_id: int
    question_id: int
    answer_text: str
    answer_score: int
    is_copy_paste: bool | False
    answered_in_seconds: str
    question_prompt: str


class StartTestRequest(BaseModel):
    user_id: int

class QuestionBatch(BaseModel):
    batch_id: int
    batch_number: int
    tier: str | None
    questions: List[Question]  # Define the Question model based on your needs

class SubmitAnswers(BaseModel):
    user_id: int
    trait: str
    answers: List[Answer]  # Define the Answer model based on your needs

class User(BaseModel):
    user_id: int
    email: EmailStr
    tier_type: str | None
    user_status: str | None
    swipe_count: int | None
    swipe_limit: int | None
    sex: str | None
    country: str | None
    auth_provider_id: int
    family_name: str | None
    given_name: str | None
    locale: str | None

class UserSession(BaseModel):
    user_id: int
    batch_number: int
    isCompleted: bool
    # add more fields
    score: int | None
