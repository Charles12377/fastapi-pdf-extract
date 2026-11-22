"""
FastAPI 可以识别同时声明的多个路径参数和查询参数。

而且声明这些参数的顺序并不重要。

FastAPI 通过参数名进行检测：
"""


from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item