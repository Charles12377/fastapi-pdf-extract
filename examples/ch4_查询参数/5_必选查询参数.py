"""
为不是路径参数的参数声明默认值（至此，仅有查询参数），该参数就不是必选的了。

如果只想把参数设为可选，但又不想指定参数的值，则要把默认值设为 None。

如果要把查询参数设置为必选，就不要声明默认值：
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item