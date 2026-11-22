"""
有时，路径操作中的路径是写死的。

比如要使用 /users/me 获取当前用户的数据。

然后还要使用 /users/{user_id}，通过用户 ID 获取指定用户的数据。

由于路径操作是按顺序依次运行的，因此，一定要在 /users/{user_id} 之前声明 /users/me ：
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


"""同样，你不能重复定义一个路径操作："""
#由于路径首先匹配，始终会使用第一个定义的

from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]