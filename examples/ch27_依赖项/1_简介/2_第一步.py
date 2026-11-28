
from typing import Annotated

#导入 Depends
from fastapi import Depends, FastAPI

app = FastAPI()

#创建依赖项，或"dependable"
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

#在“dependant”中声明依赖项

@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons