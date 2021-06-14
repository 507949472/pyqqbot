from indao.common import *
from indao.mingling import clml
from shijian import messagee,noticee,requeste

def getcl(a):
    ptype=pst(a)
    if ptype == "message":
        if clml(a):
            messagee.domsge(a)
    elif ptype == "notice":
        noticee.dontce(a)
    elif ptype == "request":
        requeste.doreqe(a)
    else:
        return 0
