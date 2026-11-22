"""直接使用 Starlette 的选项，就可以用如下 URL 声明包含路径的路径参数："""

from fastapi import FastAPI

app=FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path:str):
    return {"file_path":file_path}