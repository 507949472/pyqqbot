from outdao.doapi import sgm, sgar,sgc
from indao.common import *

def doreqe(a):
    rtype=rqt(a)
    if rtype == "group":
        gid=qgi(a)
        uid=qui(a)
        stype=sbt(a)
        comm=qcom(a)
        flag=qflag(a)
        if "梦程" in comm:
            sgar(flag,True,stype)
            sgc(gid,uid)
        else:
            sgar(flag,False,stype,"验证信息错误")

