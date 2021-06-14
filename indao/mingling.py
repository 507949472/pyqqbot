from functools import wraps

from indao.common import *
from outdao.doapi import sgm,spm
from shijian.mlcl import *
import json

with open("files/adminlist.json", "r", encoding="utf-8") as xmlf:
    xmls = xmlf.read()
    alis=json.loads(xmls)
    sadmin=alis["sadmin"]
    admin=alis["admin"]

# admin.append("111111")
# with open("../files/adminlist.json", "w", encoding="utf-8") as f:
#     json.dump(alis, f, ensure_ascii=False)
#
# print(alis)

def quanxian(a):
    user="u"
    if qui(a) in admin:
        user="a"
    elif qui(a) in sadmin:
        user="s"
    return user


def getml(a):
    msg=qmsg(a)
    # print(msg)
    msg=msg.split(" ",maxsplit=1)
    ml=msg[0][1:].strip()
    try:
        cs=msg[1]
        return ml,cs
    except:
        return ml,""

def tongyong(a,ml,cs):
    if ml == "help":
        dohelp(a)
        return True
    if ml == "抽奖":
        dochoujiang(a)
        return True
    if ml == "天气":
        tianqi(a,cs)
        return True
    return False


def tongyongp(a,ml,cs):
    if ml == "help":
        dohelp(a)
        return True
    elif ml == "天气":
        tianqi(a,cs)
        return True
    return False

def adminy(a,ml,cs):
    if ml == "add":
        doadd(a,cs)
        return True
    if ml == "del":
        dodel(a,cs)
        return True
    if ml == "delall":
        dodelall(a,cs)
        return True
    if ml == "list":
        dolist(a,cs)
        return True
    if ml == "禁言":
        c=cs.split("#")
        # print(cs)
        # s="[CQ:at,qq=507949472]"
        uid=c[0][10:-2]
        # print(uid)
        time=c[1]
        doban(a,uid,time)
        return True
    return False





def minglingg(a):
    ua=quanxian(a)
    ml,cs=getml(a)
    if ua == "s":
        if tongyong(a,ml,cs):
            return 0
        elif adminy(a,ml,cs):
            return 0
        elif ml == "addmin":
            admin.append(str(cs))
            with open("files/adminlist.json", "w", encoding="utf-8") as f:
                json.dump(alis, f, ensure_ascii=False)
            sgm(qgi(a),"添加管理员成功了喵！！！")
        else:
            sgm(qgi(a),"没有该命令啊！！！")
    elif ua == "a":
        if tongyong(a,ml,cs):
            return 0
        if adminy(a,ml,cs):
            return 0
        sgm(qgi(a),"没有该命令或无权执行，请联系主人啊喵")
    else:
        if tongyong(a,ml,cs):
            return 0
        sgm(qgi(a),"没有该命令或无权执行，请联系主人啊喵")

def minglingp(a):
    ua=quanxian(a)
    ml,cs=getml(a)
    if ua == "s":
        if tongyongp(a,ml,cs):
            return 0
        elif adminy(a,ml,cs):
            return 0
        elif ml == "addadmin":
            admin.append(str(cs))
            with open("files/adminlist.json", "w", encoding="utf-8") as f:
                json.dump(alis, f, ensure_ascii=False)
            spm(qui(a),"添加管理员成功了喵！！！")
        else:
            spm(qui(a),"没有该命令啊！！！")
    elif ua == "a":
        if tongyongp(a,ml,cs):
            return 0
        elif adminy(a,ml,cs):
            return 0
        spm(qui(a),"没有该命令或无权执行，请联系主人啊喵")
    else:
        if tongyongp(a,ml,cs):
            return 0
        spm(qui(a),"没有该命令或无权执行，请联系主人啊喵")



def clml(a):
    if qmsg(a)[0] == "#":
        # print("#")
        mtype=mst(a)
        # print(mtype)
        if mtype == "private":
            minglingp(a)
        if mtype == "group":
            minglingg(a)
        return False
    return True



