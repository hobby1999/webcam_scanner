from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.filepathforchecksec import get_filepaths
from func_common.process_exec import cmd
from func_common.crawl import crawl


@router.get("/cvelookup",description="cve查找，username为用户名，filename为固件名称",name="根据厂商查找Cve")
async def cvelookup(username,filename):
    try:
        cve_result = []
        file_tmp_name = filename.rsplit(".",-1)[0]
        company_dict = open("dict/company.txt",'r')
        dict_data = company_dict.readlines()
        result = str
        for data in dict_data:
            if data.split(":")[0] == file_tmp_name:
                result = data.split(":")[1]
        cve_result = crawl(keyword=result)
        if cve_result is not None:
            return  {"code":"200","status":True,"msg":cve_result,"datetime":getcurrenttime()}
        else:
            return {"code":"503","status":False,"msg":"未找到有效CVE编号","datetime":getcurrenttime()}
    except:
        return {"code":"200","status":False,"msg":"未知错误","datetime":getcurrenttime()}