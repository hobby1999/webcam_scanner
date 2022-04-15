from fastapi import APIRouter
'''
API路由蓝图
'''
router = APIRouter()

from api_common import api_download
from api_common import api_uploadfile
from api_common import api_delete
from plugins import api_cvelookup
from plugins import api_checkenvironment
from plugins import api_checkcompany
from plugins import api_passwdcheck
from plugins import api_checksec
from plugins import api_simplescan
from plugins import api_binwalk_all
from plugins import api_binwalk_encrpt
from plugins import api_extract
from plugins import api_filetree
