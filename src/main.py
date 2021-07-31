from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId
from typing import Optional
import json

app = FastAPI()

client = MongoClient("mongodb://mongo:27017")
db = client['mairu']
quote_collection = db['quotes']
question_collection = db['questions']


class Quote(BaseModel):
    _id: ObjectId
    quote: str
    quote_by: str
    ref: Optional[str]
    media_url: Optional[str]
    media_type: Optional[str]


class Question(BaseModel):
    _id: ObjectId
    question: str


class QuestionPostRequest(BaseModel):
    question: str
    jingjung: bool


@app.get("/")
async def get_mairu_quote():
    """ return json of mairu quote """
    single_result = quote_collection.find_one(
        {"_id": ObjectId("6104dd41692707e716e2ddf6")})  # 🥚 I don't know what to find `mairu mairu mairu`
    quote = Quote(**single_result)
    return quote


@app.get("/questions")
async def get_all_question():
    """ return array of questions """
    questions = []
    cursor = question_collection.find()
    for doc in cursor:
        questions.append(Question(**doc))
    return {"questions": questions}


@app.get("/question")
async def get_random_question():
    """ return json of random question """
    cursor = question_collection.aggregate([{"$sample": {"size": 1}}])
    for doc in cursor:
        question = Question(**doc)
    return question


@app.get("/question/{id}")
async def get_question_from_id(id):
    """ return json of question from specific id """
    single_result = question_collection.find_one({"_id": ObjectId(id)})
    question = Question(**single_result)
    return question


@app.post("/question")
async def get_answer(question: QuestionPostRequest):
    """ return answer quote from question """
    if question.question != "":
        question_collection.insert_one(question.dict())
    if question.jingjung:
        cursor = quote_collection.aggregate([{"$sample": {"size": 1}}])
        for doc in cursor:
            quote = Quote(**doc)
    else:
        single_result = quote_collection.find_one(
            {"_id": ObjectId("6104dd41692707e716e2ddf6")})
        quote = Quote(**single_result)
    return quote


@app.get("/quotes")
async def get_all_quotes():
    """ return array of quotes """
    quotes = []
    cursor = quote_collection.find()
    for doc in cursor:
        quotes.append(Quote(**doc))
    return {"quotes": quotes}


@app.get("/quote")
async def get_random_quote():
    """ return json of random quote """
    cursor = quote_collection.aggregate([{"$sample": {"size": 1}}])
    for doc in cursor:
        quote = Quote(**doc)
    return quote


@app.get("/quote/{id}")
async def get_quote_from_id(id):
    """ return json of quote from specific id """
    single_result = quote_collection.find_one({"_id": ObjectId(id)})
    quote = Quote(**single_result)
    return quote


@app.post("/quote")
async def get_answer(quote: Quote):
    """ return answer quote from quote """
    quote_collection.insert_one(quote.dict())
    return {"message": "inserted"}
