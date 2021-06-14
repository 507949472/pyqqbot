from outdao.doapi import spm, sgm
import json
import random

def querycom(msg):
    xmlf = open("files/common.json", "r", encoding="utf-8")
    xmls = xmlf.read()
    com = json.loads(xmls)
    try:
        listr=com[msg]
        res=random.choice(listr)
        print(res)
        return res
    except:
        for i in com:
            if i in msg:
                listr=com[i]
                res=random.choice(listr)
                print(res)
                return res
            else:
                return 0

def repm(uid, msg):
    remsg = querycom(msg)
    print(remsg)
    if remsg:
        spm(uid,remsg)

def regm(gid, msg):
    remsg = querycom(msg)
    print(remsg)
    if remsg:
        sgm(gid,remsg)

if __name__ == '__main__':
    repm(1, 2)
