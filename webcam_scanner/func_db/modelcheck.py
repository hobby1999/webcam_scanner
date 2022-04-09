from pydantic import BaseModel

class PasswdDictBase(BaseModel):
    original_password:str
    know_password:str
   

class PasswdDict(PasswdDictBase):
    id:int
    class Config:
        orm_mode = True

class FirmwareTypeBase(BaseModel):
    company:str
    firmwaretags:str


class FirmwareType(FirmwareTypeBase):
    id:int
    class Config:
        orm_mode = True

