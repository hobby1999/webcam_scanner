from fastapi import FastAPI
from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from starlette.responses import FileResponse
import os

@router.get("/downloadfile",name="文件下载接口",description="下载文件API，username为用户名，filename为需要下载的固件名称")
async def downloadfile(username,filename):
    file_tmp_path = filename.rsplit(".",1)[0]
    file_path = f"firmware/tmp/{username}/{file_tmp_path}/{filename}"
    try:
        if os.path.isfile(file_path):
            return FileResponse(path=file_path,filename=filename)
        else:
            return {"code":"503","status":False,"msg":"文件不存在","datetime":getcurrenttime()}
    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}