"""
在上面的示例中，你会发现这里有一点点代码重复。

当你需要使用 common_parameters() 这个依赖时，你必须写出完整的带类型注解和 Depends() 的参数：


commons: Annotated[dict, Depends(common_parameters)]
但因为我们使用了 Annotated，可以把这个 Annotated 的值存到一个变量里，在多个地方复用：
"""

from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


CommonsDep = Annotated[dict, Depends(common_parameters)]


@app.get("/items/")
async def read_items(commons: CommonsDep):
    return commons


@app.get("/users/")
async def read_users(commons: CommonsDep):
    return commons