from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.filepathforchecksec import get_filepaths
from func_common.process_exec import cmd


@router.get("/checkenviroment",description="检查运行时环境,username为用户名，filename为固件名称",name="运行服务检查")
async def checkenviroment(username,filename):
    try:
        file_tmp_path = filename.rsplit(".",1)[0]
        file_path = f"firmware/extract/{username}/{file_tmp_path}/_{filename}.extracted"
        file_path_list = get_filepaths(file_path)
        bin_path = f"firmware/tmp/{username}/{file_tmp_path}/{filename}"
        args = f"strings {bin_path} | head"
        strings_result = cmd(args).rsplit("\n",-1)
        envkeyword_dict = open("dict/envkeyword.txt",'r')
        dict_data = envkeyword_dict.readlines()
        subdir = str
        subddir_list = []
        keyword = []
        for item in file_path_list:
            if item.split("/",-1)[-2] == "squashfs-root":
                subdir = item.rsplit("/",1)[0]
        subddir_list = get_filepaths(subdir)
        for item in subddir_list:
            for key in dict_data:
                if str(item).rsplit("/",1)[-1] == key.rsplit("\n",-1)[0]:
                    keyword.append(key.rsplit("\n",-1)[0])
        for item in strings_result:
            for key in dict_data:
                if item == key.rsplit("\n",-1)[0]:
                    keyword.append(key.rsplit("\n",-1)[0])
        return {"code":"200","status":True,"msg":keyword,"datetime":getcurrenttime()}
    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}
