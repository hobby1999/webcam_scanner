from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.process_exec import cmd
import os
import shutil

@router.get("/extract",description="使用Binwalk -Me对固件进行递归解压，username参数为用户名,filename参数为上传固件的名字",name="固件释放")
async def extract(username,filename):
    try:
        file_tmp_path = filename.rsplit(".",1)[0]
        extract_path = f"firmware/extract/{username}/{file_tmp_path}/_{filename}.extracted"
        if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{filename}"):
            args = f"binwalk -Me  firmware/tmp/{username}/{file_tmp_path}/{filename} -C firmware/extract/{username}/{file_tmp_path}/" #binwalk释放固件
            if os.path.isdir(extract_path):
                shutil.rmtree(extract_path)
            if cmd(args) != "error":
                return {"code":"200","status":True,"msg":"文件释放完成","datetime":getcurrenttime()}
            else:
                return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}
        else:
            return {"code":"500","status":False,"msg":"文件不存在","datetime":getcurrenttime()}
    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}