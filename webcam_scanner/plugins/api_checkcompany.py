from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime


@router.get("/checkcompany",description="检查固件厂商，filename为固件名称",name="检查固件的厂商")
async def checkcompany(filename):
    try:
        file_tmp_name = filename.rsplit(".",-1)[0]
        company_dict = open("dict/company.txt",'r')
        dict_data = company_dict.readlines()
        result = str
        for data in dict_data:
            if data.split(":")[0] == file_tmp_name:
                result = data.split(":")[1]
        if result:
            return {"code":"200","status":True,"msg":result,"datetime":getcurrenttime()}
        else:
            return {"code":"503","status":False,"msg":"未知厂商","datetime":getcurrenttime()}
    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}

