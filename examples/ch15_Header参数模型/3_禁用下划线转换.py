"""
与常规的 header 参数相同，当参数名中包含下划线时，会自动转换为连字符。

例如，如果你的代码中有一个名为 save_data 的 header 参数，那么预期的 HTTP 头将是 save-data，并且在文档中也会以这种形式显示。

如果由于某些原因你需要禁用这种自动转换，你也可以在用于 header 参数的 Pydantic 模型中进行设置。
"""

from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(
    headers: Annotated[CommonHeaders, Header(convert_underscores=False)],
):
    return headers
