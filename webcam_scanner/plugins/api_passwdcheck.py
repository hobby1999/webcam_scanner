from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.filepathforchecksec import get_filepaths
import os

@router.get("/checkpasswd",
name="账号密码检查",
description="用于账号密码检查的api，查看是否有弱密码流出,username为用户名参数，filename为文件参数")
async def checkpasswd(username,filename):
    file_tmp_path = filename.rsplit(".",1)[0]
    filepath = f"firmware/extract/{username}/{file_tmp_path}/_{filename}.extracted"
    passwd_path_result = []
    shadow_path_result = []
    passwd_result = []
    shadow_result = []
    try:
        if os.path.isdir(filepath):
          
          filepath_result =  get_filepaths(filepath)
          for i in filepath_result:
            if i.split('/')[len(i.split('/'))-1] == "passwd":
                passwd_path_result.append(i)
                print(passwd_path_result)
            if i.split('/')[len(i.split('/'))-1] == "shadow":
                shadow_path_result.append(i)
        f = open(passwd_path_result[0],"rb")
        for line in f.readlines():
            passwd_result.append(line.rsplit("\n")[0])
        for i in passwd_result:
            print(i.split(':'))
    except:
        pass
    pass
