from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
import os

@router.get("/delete",name="文件删除接口",description="文件删除API，username为用户名，filename为需要删除的固件")
async def deletefimware(username,filename):
    file_tmp_path = filename.rsplit(".",1)[0]
    try:
        print(f"firmware/tmp/{username}/{file_tmp_path}/{filename}")
        if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{filename}"):
            os.remove(f"firmware/tmp/{username}/{file_tmp_path}/{filename}")
            if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{filename}.png"):
                os.remove(f"firmware/tmp/{username}/{file_tmp_path}/{filename}.png")
            else:
                return {"code":"200","status":True,"msg":"删除成功","datetime":getcurrenttime()}
        else:
            return {"code":"503","status":False,"msg":"该文件不存在","datetime":getcurrenttime()}
    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}   