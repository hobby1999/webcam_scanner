from turtle import st
from unittest import result
from func_db.modelcheck import PasswdDictBase,FirmwareTypeBase
from func_db.model import M_FirmwareType,M_PasswdDict
from sqlalchemy.orm import Session

class funcs:
    @staticmethod
    def get_passwd(db:Session,firmwarepasswd:str):
        result = db.query(M_PasswdDict).filter(M_PasswdDict.original_password == firmwarepasswd).first()
        return result
    
    @staticmethod
    def new_passwd_data(db:Session,passwddata:PasswdDictBase):
        db_passwd = M_PasswdDict(original_password=passwddata.original_password,know_password=passwddata.know_password)
        db.add(db_passwd)
        db.commit()
        db.refresh()
        return db_passwd
    
    @staticmethod
    def get_company(db:Session,firmwaretags:str):
        result = db.query(M_FirmwareType).filter(M_FirmwareType.firmwaretags == firmwaretags).first()
        return result

    @staticmethod
    def new_company(db:Session,companydata:FirmwareTypeBase):
        db_company = M_FirmwareType(company=companydata.company,firmwaretags=companydata.firmwaretags)
        db.add(db_company)
        db.commit()
        db.refresh()
        return db_company 