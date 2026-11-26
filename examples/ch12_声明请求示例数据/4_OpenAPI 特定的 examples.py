"""
使用 openapi_examples 参数¶
你可以在 FastAPI 中通过参数 openapi_examples 来声明这个 OpenAPI 特定的 examples，适用于：

Path()
Query()
Header()
Cookie()
Body()
Form()
File()
这个 dict 的键用于标识每个示例，每个值是另一个 dict。

examples 中每个具体示例的 dict 可以包含：

summary：该示例的简短描述。
description：较长描述，可以包含 Markdown 文本。
value：实际展示的示例，例如一个 dict。
externalValue：value 的替代项，指向该示例的 URL。不过它的工具支持度可能不如 value。
"""

from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            openapi_examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results