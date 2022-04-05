from fastapi import FastAPI
import uvicorn
from api_common import api_router
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()


'''
核心启动程序
'''


'''
app路由，路由文件为api_router
'''
app.include_router(api_router.router,prefix="/api")


'''跨域设置'''
origins = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,  #设置允许的origins来源
    allow_credentials=True,
    allow_methods=["*"],  # 设置允许跨域的http方法，比如 get、post、put等。
    allow_headers=["*"])  #允许跨域的headers，可以用来鉴别来源等作用。

@app.get("/")
async def root():
    return {"msg":"hello"}

