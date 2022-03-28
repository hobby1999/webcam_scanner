from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.process_exec import cmd
import os

@router.get("/checksec",description="使用gdb checksec进行对固件系统中的二进制程序进行保护检查，username为用户名参数，filename为固件名参数",name="checksec检查")
async def checksec(username,filename):
    pass
