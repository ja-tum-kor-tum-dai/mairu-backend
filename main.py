from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from random import choice

app = FastAPI()

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_mairu_quote():
    """ return json of mairu quote """
    with open('mairu.txt', 'r', encoding='utf-8') as reader:
        mairus = reader.read().split('\n')
        if mairus[-1] == '':
            mairus.pop()
    sample_mairu = choice(mairus)
    quote = {
        "quote": sample_mairu,
    }
    return quote
