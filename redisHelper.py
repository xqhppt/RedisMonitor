# coding=utf-8
import json
import redis

rDict = {}


def getConfigList():
    f = file('conf/redis.json',mode='r')
    s = None

    try:
        s = json.load(f)
    finally:
        f.close()

    return s


rList = getConfigList()

#获取redis对象
def getRedis(host,port,password):
    global rDict
    key = host + ":" + port

    if rDict.has_key(key):
        r = rDict[key]
    else:
        if password != '':
            r = redis.StrictRedis(host =host, port =port, db = 0, password=password)
        else:
            r = redis.StrictRedis(host =host, port =port, db = 0)

        rDict[key] = r
    return  r

#info
def getRedisDetail(host,port,password):
    r = getRedis(host,port,password)

    return  r.info()
