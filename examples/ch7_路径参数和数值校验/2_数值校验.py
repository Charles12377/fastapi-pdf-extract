from typing import Annotated

from fastapi import FastAPI,Path

app=FastAPI()


@app.get("/items/{item_id}")
#大于等于
async def read_items(
    item_id:Annotated[int,Path(title="The ID of the item to get",ge=1)],q:str
):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    return results

#大于和小于等于
from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id:Annotated[int,Path(title="The ID of the item to  get",gt=0,le=1000)],
    q:str
):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    return results



#浮点数、大于和小于
from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id:Annotated[int,Path(title="The ID of the item to get",ge=0,le=1000)],
    q:str,
    size:Annotated[float,Query(gt=0,lt=10.5)],
):
    results={"item_id":item_id}
    if q:
        results.update({"q":q})
    if size:
        results.update({"size":size})
    return results