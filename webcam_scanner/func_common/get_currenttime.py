import datetime

'''
获取当前时间
'''

def getcurrenttime():
    return datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')