import requests

urlf="http://127.0.0.1:5700/"


def link(url,data):
    res=requests.post(url,data).text
    return res


def spm(uid,msg):
    url=urlf+"send_private_msg"
    data={
            "user_id":uid,
            "message":msg
          }
    res=link(url,data)
    return res


def sgm(gid,msg):
    url=urlf+"send_group_msg"
    data={
        "group_id":gid,
        "message":msg
    }
    res=link(url,data)
    return res

def sgar(flag,app,sbt,why=""):
    url=urlf+"set_group_add_request"
    data={
        "flag":flag,
        "sub_type":sbt,
        "approve":app,
        "reason":why
    }
    res=link(url,data)
    return res

def sgc(gid,uid,card=""):
    url=urlf+"set_group_card"
    data={
        "group_id":gid,
        "user_id":uid,
        "card":card,
    }
    res=link(url,data)
    return res


def ban(gid,uid,time="1"):
    url=urlf+"set_group_ban"
    data={
        "group_id":gid,
        "user_id":uid,
        "duration":int(time)*60,
    }
    res=link(url,data)
    return res


if __name__ == '__main__':
    a=spm(507949472,"你好")
    print(a)