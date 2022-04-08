knowpasswd_result = []

def checkKnowPasswd(passwd):
    fileopen = open("/home/cheng/webcam_scanner/webcam_scanner/dict/knowpasswd","r")
    for line in fileopen.readlines():
        knowpasswd_result.append(line.rsplit("\n")[0])
    for line in knowpasswd_result:
        if line.split(":")[0] == passwd:
            return line.split(":")[1]
