#coding:utf-8

from enum import Enum, unique

@unique
class FileStatus(Enum):
    # 上传文件
    waitToUpload = 20
    onUpload = 21
    uploadSuccess = 221
    uploadFailure = 222
    uploadCancel = 223
    uploadSuspend = 23
    # 渲染
    onQueue = 60
    onRendering = 61
    renderSuccess = 621
    renderFailure = 622
    renderCancel = 623
    renderSuspend = 63
