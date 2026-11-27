from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class FormDate(BaseModel):
    username:str
    password:str


@app.post("/login/")
async def login(date:Annotated[FormDate,Form()]):
    return date