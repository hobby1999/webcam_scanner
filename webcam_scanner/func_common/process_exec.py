import os
import signal
from subprocess import Popen, PIPE, TimeoutExpired

"""
调用Linux Shell进行系统调用
"""
#subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
#subp.wait(50)
#if subp.poll() == 0:
#    return subp.communicate()[0]
#else:
#    return "error"

def cmd(command):
    with Popen(command,shell=True,stdout=PIPE,preexec_fn=os.setsid,encoding="utf-8") as process:
        try:
            output = process.communicate(timeout=50)[0]
            return output
        except TimeoutExpired:
            os.killpg(process.pid, signal.SIGINT)
            return "error"
        