from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_db.dbconnect import getdb
from func_db.query import funcs
from func_db.model import *
from fastapi import Depends
from sqlalchemy.orm import Session

@router.get("/checkcompany",description="检查固件厂商，filename为固件名称，username为用户名",name="检查固件的厂商")
async def checkcompany(filename,db:Session=Depends(getdb)):
    try:
        file_tmp_name = filename.rsplit(".",-1)[0]
        db_result = funcs.get_company(db,firmwaretags=file_tmp_name)
        if db_result:
            return {"code":"200","status":True,"msg":db_result.company,"datetime":getcurrenttime()}
        else:
            return {"code":"503","status":False,"msg":"未知厂商","datetime":getcurrenttime()}
    except:
        return {"code":"500","status":False,"msg":"未知错误","datetime":getcurrenttime()}

