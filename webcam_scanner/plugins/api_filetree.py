from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
from func_common.filetree import tree_to_json
import os

@router.get("/filetree",description="文件树展示，useranme为用户名参数，filename为固件名",name="文件树展示")
async def filetree(username,filename):
    file_tmp_path = filename.rsplit(".",1)[0]
    filepath = f"firmware/extract/{username}/{file_tmp_path}/_{filename}.extracted"
    try:
        if os.path.isdir(filepath):
            result = tree_to_json(filepath)
            return {"code":"200","status":True,"msg":result,"datetime":getcurrenttime()}
    except:
        pass
    pass
