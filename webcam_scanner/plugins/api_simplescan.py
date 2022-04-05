from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.process_exec import cmd

'''
File命令进行文件简单信息检测接口
'''
@router.get("/simplescan",description="利用File进行文件简单分析，上传后可使用，filename传值为上传的固件名称",name="file简单分析")
async def simplescan(username,filename):
    file_tmp_path = filename.rsplit(".",1)[0]
    args = f"file firmware/tmp/{username}/{file_tmp_path}/{filename}"
    result = cmd(args).split(": ",1)[1].rsplit("\n")[0]#输出的信息处理
    try:
        if result != "error":
            return {"code":"200","status":True,"msg":result,"datetime":getcurrenttime(),}
        else:
            return {"code":"503","status":False,"msg":"无法执行命令","datetime":getcurrenttime()}
    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}

