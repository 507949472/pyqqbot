def pst(a):
    try:
        res=a["post_type"]
        return res
    except:
        return ""

def mst(a):
    try:
        res=a["message_type"]
        return res
    except:
        return ""

def ntt(a):
    try:
        res=a["notice_type"]
        return res
    except:
        return ""

def rqt(a):
    try:
        res=a["request_type"]
        return res
    except:
        return ""

def qcom(a):
    try:
        res=a["comment"]
        return res
    except:
        return ""

def qflag(a):
    try:
        res=a["flag"]
        return res
    except:
        return ""

def sbt(a):
    try:
        res=a["sub_type"]
        return res
    except:
        return ""

def qgi(a):
    try:
        res=a["group_id"]
        return res
    except:
        return ""

def qui(a):
    try:
        res=a["user_id"]
        return str(res)
    except:
        return ""

def qmsg(a):
    try:
        res=a["message"]
        return res
    except:
        return ""