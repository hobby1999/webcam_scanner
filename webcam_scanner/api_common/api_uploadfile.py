from api_common.api_router import router
from func_common.get_currenttime import getcurrenttime
import os
import shutil
from fastapi import UploadFile,File


'''
文件上传接口
'''
@router.post("/uploadfile",name="文件上传接口",description="文件上传API，username为用户名，file为要上传的文件数据")
async def uploadfile(username,file:UploadFile = File(...)):
    filename_ext = file.filename.split(".")[len(file.filename.split('.'))-1]
    file_tmp_path = file.filename.rsplit(".",1)[0]
    ext = ["bin","tar","trx","tar","tar.gz"]
    try:
        for i in ext:
            if filename_ext != i:
                return {"code":"503","status":False,"msg":"后缀不符合要求","datetime":getcurrenttime()}
            else:
                if os.path.isdir(f"firmware/tmp/{username}/"):
                    if os.path.isdir(f"firmware/tmp/{username}/{file_tmp_path}"):
                        with open(f'{file.filename}',"wb") as buffer:
                            shutil.copyfileobj(file.file,buffer)
                            if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}"):
                                os.remove(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                                shutil.move(file.filename,f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                            else:
                                shutil.move(file.filename,f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                        if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}"):
                            return {"code":"200","status":True,"msg":"上传成功","datetime":getcurrenttime()}
                        else:
                            return {"code":"503","status":True,"msg":"上传不成功","datetime":getcurrenttime()}
                    else:
                        os.mkdir(f"firmware/tmp/{username}/{file_tmp_path}")
                        with open(f'{file.filename}',"wb") as buffer:
                            shutil.copyfileobj(file.file,buffer)
                            if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}"):
                                os.remove(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                                shutil.move(file.filename,f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                            else:
                                shutil.move(file.filename,f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                        if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}"):
                            return {"code":"200","status":True,"msg":"上传成功","datetime":getcurrenttime()}
                        else:
                            return {"code":"503","status":True,"msg":"上传不成功","datetime":getcurrenttime()}
                else:
                    os.mkdir(f"firmware/tmp/{username}/")
                    if os.path.isdir(f"firmware/tmp/{username}/{file_tmp_path}"):
                        with open(f'{file.filename}',"wb") as buffer:
                            shutil.copyfileobj(file.file,buffer)
                            if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}"):
                                os.remove(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                                shutil.move(file.filename,f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                            else:
                                shutil.move(file.filename,f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                        if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}"):
                            return {"code":"200","status":True,"msg":"上传成功","datetime":getcurrenttime()}
                        else:
                            return {"code":"503","status":True,"msg":"上传不成功","datetime":getcurrenttime()}
                    else:
                        os.mkdir(f"firmware/tmp/{username}/{file_tmp_path}")
                        with open(f'{file.filename}',"wb") as buffer:
                            shutil.copyfileobj(file.file,buffer)
                            if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}"):
                                os.remove(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                                shutil.move(file.filename,f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                            else:
                                shutil.move(file.filename,f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}")
                        if os.path.isfile(f"firmware/tmp/{username}/{file_tmp_path}/{file.filename}"):
                            return {"code":"200","status":True,"msg":"上传成功","datetime":getcurrenttime()}
                        else:
                            return {"code":"503","status":True,"msg":"上传不成功","datetime":getcurrenttime()}
    except:
        return {"code":"500","status":True,"msg":"未知错误","datetime":getcurrenttime()}