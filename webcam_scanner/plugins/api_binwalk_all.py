from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.process_exec import cmd


@router.get("/binwalk_all",description="Binwalk全面分析,会输出Binwalk -B的全部内容，上传后可利用,filename传值为上传的固件名称",name="Binwalk全面分析")
async def binwallall(username,filename):
    file_tmp_path = filename.rsplit(".",1)[0]
    args = f"binwalk -B firmware/tmp/{username}/{file_tmp_path}/{filename}"
    try:
        if cmd(args) == "error":
            return {"code":"500","status":False,"msg":"分析出错，请验明固件是否被加密或不完整","datetime":getcurrenttime()}
        else:
            result = cmd(args).rsplit("\n",maxsplit=-1)
            result = [i for i in result if i != '']
            if result[3] == "":
                return {"code":"503","status":False,"msg":"分析出错，请验明固件是否被加密或不完整","datetime":getcurrenttime()}
            else:
                return {"code":"200","status":True,"msg":result,"datetime":getcurrenttime()}
    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}
