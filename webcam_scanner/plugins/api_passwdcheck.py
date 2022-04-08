from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.filepathforchecksec import get_filepaths
from func_common.passwdcheck import checkKnowPasswd
import os

'''
弱口令检测API，不包含暴力枚举破解，只进行收集弱口令检测
'''
@router.get("/checkpasswd",
name="账号密码检查",
description="用于账号密码检查的api，查看是否有弱密码泄露,username为用户名参数，filename为文件参数")
async def checkpasswd(username,filename):
    file_tmp_path = filename.rsplit(".",1)[0]
    filepath = f"firmware/extract/{username}/{file_tmp_path}/_{filename}.extracted"
    passwd_path_result = []
    shadow_path_result = []
    passwd_result = []
    shadow_result = []
    final_result = []
    try:
        if os.path.isdir(filepath):
          
          filepath_result =  get_filepaths(filepath)
          for i in filepath_result:
            if i.split('/')[len(i.split('/'))-1] == "passwd":
                passwd_path_result.append(i)
            if i.split('/')[len(i.split('/'))-1] == "shadow":
                shadow_path_result.append(i)
        if passwd_path_result:
            passwd_fopen = open(passwd_path_result[0],"r")
        if shadow_path_result:
            shadow_fopen = open(shadow_path_result[0],"r")
        for line in passwd_fopen.readlines():
            passwd_result.append(line.rsplit("\n")[0])
        for line in shadow_fopen.readlines():
            shadow_result.append(line.rsplit("\n")[0])
        print(shadow_result)
        for passwordline in passwd_result:
            if passwordline.split(':')[1] == "":
                final_result.append(passwordline.split(":")[0] + "高危，此账号未设置密码")
            elif passwordline.split(':')[1] == "*":
                final_result.append(passwordline.split(":")[0] + "此账户密码经过加密")
            elif passwordline.split(':')[1] == "!":
                final_result.append(passwordline.split(":")[0] + "此账户密码经过加密")
            elif passwordline.split(':')[1] == "x":
                for shadowline in shadow_result:
                    if shadowline.split(":")[0] == passwordline.split(":")[0]:
                        if checkKnowPasswd(shadowline.split(":")[1]):
                            final_result.append(passwordline.split(":")[0] + "密码是:" + checkKnowPasswd(shadowline.split(":")[1]))
        if final_result is not None:
            return {"code":"200","status":True,"msg":final_result,"datetime":getcurrenttime()}
        else:
            return {"code":"503","status":False,"msg":"未找到泄露密码","datetime":getcurrenttime()}

    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}
