from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q:Annotated[list[str]|None,Query()]=None):
    Query_items={"q":q}
    return Query_items

"""
具有默认值的查询参数列表 / 多个值
"""
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

"""只是用list"""
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q:Annotated[list,Query()]=[]):
    query_items={"q":q}
    return query_items