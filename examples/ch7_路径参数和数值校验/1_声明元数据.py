from typing import Annotated

from fastapi import FastAPI,Path,Query

app=FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id:Annotated[int,Path(title="The ID of the item to get")],
    q:Annotated{str|None,Query(alias="item-query")}=None,
):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    return results


#无annotated，q无默认值(无默认值的参数需要在有默认值的参数之前)
from fastapi import FastAPI,Path

app=FastAPI()


@app.get("/items/{item_id}")
async def read_items(q:str,item_id:int=Path(title="The ID of the item to get")):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    return results