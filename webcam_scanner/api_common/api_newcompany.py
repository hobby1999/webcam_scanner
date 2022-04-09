from func_db.dbconnect import getdb
from func_db.query import funcs
from func_db.modelcheck import FirmwareTypeBase,FirmwareType
from func_db.model import *
from api_common.api_router import router
from fastapi import Depends
from sqlalchemy.orm import Session

@router.post("/newcompany",response_model=FirmwareType,description="用于更新固件厂商至数据库",name="更新固件产厂商")
async def newcompany(newdata:FirmwareTypeBase,db:Session = Depends(getdb)):
    return funcs.new_company(db=db,companydata=newdata)
