from unicodedata import name
from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.filepathforchecksec import get_filepaths


@router.get("/checkpasswd",name="账号密码检查",description="用于账号密码检查的api，查看是否有弱密码流出,username为用户名参数，filename为文件参数")
async def checkpasswd(useranme,filename):
