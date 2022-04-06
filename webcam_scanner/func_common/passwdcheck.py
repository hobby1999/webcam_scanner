import hashlib
import os

knowpasswd_result = []
bruteforce_result = []

def sha1(passwd,salt):
    pass

def md5(passwd,salt):
    pass



def checkKnowPasswd(passwd):
    fileopen = open("/home/cheng/webcam_scanner/webcam_scanner/dict/knowpasswd","r")
    for line in fileopen.readlines():
        knowpasswd_result.append(line.rsplit("\n")[0])
    for line in knowpasswd_result:
        if line.split(":")[0] == passwd:
            return line.split(":")[1]

def bruteForcePasswd(passwd):
    fileopen = open("/home/cheng/webcam_scanner/webcam_scanner/dict/rainbowpasswd","r")
    for line in fileopen.readlines():
        bruteforce_result.append(line.rsplit("\n")[0])
    