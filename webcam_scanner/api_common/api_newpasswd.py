from func_db.dbconnect import getdb
from func_db.query import funcs
from func_db.modelcheck import PasswdDict,PasswdDictBase
from func_db.model import *
from api_common.api_router import router
from fastapi import Depends
from sqlalchemy.orm import Session


@router.post("/newpasswd",response_model=PasswdDict,description="用于更新新的弱口令至数据库",name="更新弱口令")
async def newpasswd(newdata:PasswdDictBase,db:Session = Depends(getdb)):
    return funcs.new_passwd_data(db=db,passwddata=newdata)
