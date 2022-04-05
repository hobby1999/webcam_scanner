from api_common.api_router import router
from fastapi.responses import FileResponse
from func_common.process_exec import cmd
from func_common.get_currenttime import getcurrenttime
import os
import shutil

@router.get("/binwalk_encrpt",description="上传后进行调用，进行熵值分析以判断固件是否加密，filename传值为上传的固件名称",name="熵值分析")
async def binwalkencrpt(username,filename):
    file_tmp_path = filename.rsplit(".",1)[0]
    try:
        if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{filename}"):
            args = f"binwalk -EJ firmware/tmp/{username}/{file_tmp_path}/{filename}"
            cmd(args)
            if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{filename}.png"):
                os.remove(f"firmware/tmp/{username}/{file_tmp_path}/{filename}.png")
                shutil.move(f"{filename}.png",f"firmware/tmp/{username}/{file_tmp_path}")
                return FileResponse(f"firmware/tmp/{username}/{file_tmp_path}/{filename}.png")
            else:
                shutil.move(f"{filename}.png",f"firmware/tmp/{username}/{file_tmp_path}")
                return FileResponse(f"firmware/tmp/{username}/{file_tmp_path}/{filename}.png")
        else:
            return {"code":"503","status":False,"msg":"文件不存在","datetime":getcurrenttime}
    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}

    
       