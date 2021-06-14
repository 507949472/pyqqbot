from indao.common import *
from outdao.dore import repm,regm

def domsge(a):
    mtype=mst(a)
    if mtype == "private":
        uid=qui(a)
        msg=qmsg(a)
        repm(uid,msg)
        res=str(uid)+":"+str(msg)
        print(res)
        return res
    elif mtype == "group":
        gid=qgi(a)
        msg=qmsg(a)
        regm(gid,msg)
        res="群 "+str(gid)+":"+str(msg)
        print(res)
        return res
    else:
        return 0