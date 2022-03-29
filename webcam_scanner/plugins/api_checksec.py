from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.process_exec import cmd
import os

@router.get("/checksec",description="使用gdb checksec进行对固件系统中的二进制程序进行保护检查，username为用户名参数，filename为固件名参数",name="checksec检查")
async def checksec(username,filename):
    file_tmp_path = filename.rsplit(".",1)[0]
    file_path = f"firmware/extract/{username}/{file_tmp_path}/_{filename}.extracted"
    try:
        if os.path.isdir(file_path):
            pass
        else:
            return {"code":"503","status":False,"msg":"找不到固件解压目录,固件有可能未解压","datetime":getcurrenttime()}
    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}
