from fastapi import FastAPI
import http
app = FastAPI()

#通过async def声明你的 路径操作函数
@app.get("/")
async def read_results():
    results=await some_library()  #等待some_library()函数操作并将结果返回results
    return results