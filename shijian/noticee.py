from outdao.doapi import sgm
from indao.common import *

def dontce(a):
    ntype=ntt(a)
    if ntype == "group_upload":
        return 0
    elif ntype == "group_admin":
        stype=sbt(a)
        if stype == "set":
            gid=qgi(a)
            uid=qui(a)
            msg="[CQ:at,qq="+str(uid)+"]"+"和群主签订了契约，成为了马猴烧酒！！！"
            sgm(gid,msg)
        elif stype == "unset":
            gid=qgi(a)
            uid=qui(a)
            msg="[CQ:at,qq="+str(uid)+"]"+"被群主解除了契约，失去了狗管理身份！！！"
            sgm(gid,msg)
    elif ntype == "group_decrease":
        gid=qgi(a)
        uid=qui(a)
        msg=str(uid)+"离开了这个世界！！！"
        sgm(gid,msg)
    elif ntype == "group_increase":
        gid=qgi(a)
        msg="欢迎啊喵~ =-="
        sgm(gid,msg)
    else:
        return 0
