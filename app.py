import sys
import os
import openai
from typing import Union

from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()


@app.post("/reply")
def post_reply(text: str):
    openai.api_key = os.environ['api_key']

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message
