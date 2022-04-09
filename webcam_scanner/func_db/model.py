from enum import unique
from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from func_db.dbconnect import engine
Base = declarative_base()

'''
弱口令对照表
'''
class M_PasswdDict(Base):
    __tablename__ = "t_passwddict"

    id = Column(Integer,primary_key=True,index=True)
    original_password = Column(String,unique=False)
    know_password = Column(String,unique=False)


'''
厂商固件对照表
'''
class M_FirmwareType(Base):
    __tablename__ = "t_firmwaretype"

    id = Column(Integer,primary_key=True,index=True)
    company = Column(String,unique=False)
    firmwaretags = Column(String,unique=True)

Base.metadata.create_all(bind=engine)