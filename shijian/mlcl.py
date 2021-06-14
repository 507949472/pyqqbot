import json
from lxml import etree

import requests
import random

from indao.common import qgi, mst, qui
from outdao.doapi import sgm, spm, ban

uals=["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/41.0.2228.0 Safari/537.36",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/41.0.2227.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/41.0.2227.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/41.0.2226.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/41.0.2225.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/41.0.2225.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/41.0.2224.3 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/40.0.2214.93 Safari/537.36",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/37.0.2049.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/36.0.1985.67 Safari/537.36",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/36.0.1985.67 Safari/537.36",
      "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/36.0.1985.125 Safari/537.36",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/35.0.3319.102 Safari/537.36",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/35.0.2309.372 Safari/537.36",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/35.0.2117.157 Safari/537.36",
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
      "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/34.0.1866.237 Safari/537.36",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/34.0.1847.137 Safari/4E423F"]

def dolink(url):
    headers={"User-Agent":random.choice(uals)}
    res=requests.get(url,headers=headers).text
    return res

with open("files/common.json", "r", encoding="utf-8") as xmlf:
    xmls = xmlf.read()
    com = json.loads(xmls)


def xh(com):
    with open("files/common.json", "w", encoding="utf-8") as f:
        json.dump(com, f, ensure_ascii=False)


def dohelp(a):
    mtype=mst(a)
    wb="命令帮助：\n#命令名 [参数]\n#help -帮助说明\n#add 关键词#回答\n#del 关键词#回答\n#delall 关键词\n#list 关键词\n#抽奖 -随机禁言套餐\n#天气 城市拼音"
    if mtype == "private":
        spm(qui(a),wb)
    elif mtype == "group":
        sgm(qgi(a),wb)

def doban(a,uid,time):
    try:
        gid=qgi(a)
        ban(gid,uid,time)
        # print("禁言 [CQ:at,qq="+str(uid)+"] "+time+"分钟")
        sgm(qgi(a),"禁言 [CQ:at,qq="+str(uid)+"] "+str(time)+"分钟")
    except Exception as e:
        print(e)
        sgm(qgi(a),"禁言失败 "+e)


def dochoujiang(a):
    time=random.randint(1,10)
    sgm(qgi(a),"抽奖成功，抽到禁言"+str(time)+"分钟")
    # print("抽奖成功，抽到禁言"+str(time)+"分钟")
    uid=qui(a)
    doban(a,uid,time)
    sgm(qgi(a),"执行完成！！！")
    # print("执行成功")


choujiang=""


def tianqi(a,cs):
    try:
        url="https://www.tianqi.com/"+cs+"/"
        html=dolink(url)
        tree=etree.HTML(html)
        div=tree.xpath("//div[@class='weatherbox']")[0]
        dl=div.xpath(".//div[@class='left']/dl")[0]
        name=dl.xpath("./dd[@class='name']/h1/text()")[0]
        time=dl.xpath("./dd[@class='week']/text()")[0]
        weather=dl.xpath("./dd[@class='weather']/span/b/text()")[0]
        wendu=dl.xpath("./dd[@class='weather']/span/text()")[0]
        shidu=dl.xpath("./dd[@class='shidu']/b[1]/text()")[0]
        wind=dl.xpath("./dd[@class='shidu']/b[2]/text()")[0]
        zwx=dl.xpath("./dd[@class='shidu']/b[3]/text()")[0]
        kq=dl.xpath("./dd[@class='kongqi']/h5/text()")[0]
        pm=dl.xpath("./dd[@class='kongqi']/h6/text()")[0]

        tqstr=name+"\n"+time+"\n"+weather+" "+wendu+"\n"+shidu+" "+wind+" "+zwx+"\n"+kq+" "+pm
        # print(tqstr)
        mtype=mst(a)
        if mtype == "private":
            spm(qui(a),tqstr)
        elif mtype == "group":
            sgm(qgi(a),tqstr)
    except Exception as eer:
        print(eer)
        mtype=mst(a)
        if mtype == "private":
            spm(qui(a),"查询失败，请稍候再试")
        elif mtype == "group":
            sgm(qgi(a),"查询失败，请稍候再试")



def doadd(a,cs):
    try:
        c=cs.split("#")
        gjc=c[0]
        ans=c[1]
        # print(gjc,ans)
        # print(com)
        try:
            com[gjc].append(ans)
            xh(com)
            mtype=mst(a)
            print(mtype)
            if mtype == "private":
                print("关键词 "+cs+" 添加成功")
                spm(qui(a),"关键词 "+cs+" 添加成功")
            elif mtype == "group":
                sgm(qgi(a),"关键词 "+cs+" 添加成功")
                # print(com[gjc])
        except:
            com[gjc]=[ans]
            xh(com)
            mtype=mst(a)
            if mtype == "private":
                spm(qui(a),"关键词 "+cs+" 添加成功")
            elif mtype == "group":
                sgm(qgi(a),"关键词 "+cs+" 添加成功")
            # print(com[gjc])
    except Exception as e:
        print(e)
        mtype=mst(a)
        if mtype == "private":
            spm(qui(a),"命令或参数有误")
        elif mtype == "group":
            sgm(qgi(a),"命令或参数有误")
            # print("命令或参数有误")


def dodel(a,cs):
    try:
        c=cs.split("#")
        gjc=c[0]
        ans=c[1]
        # print(com)
        try:
            com[gjc].remove(ans)
            xh(com)
            mtype=mst(a)
            if mtype == "private":
                spm(qui(a),"回答 "+cs+" 删除成功")
            elif mtype == "group":
                sgm(qgi(a),"回答 "+cs+" 删除成功")
            # print(com[gjc])
        except:
            mtype=mst(a)
            if mtype == "private":
                spm(qui(a),"没有这个回答，你在删空气？")
            elif mtype == "group":
                sgm(qgi(a),"没有这个回答，你在删空气？")
    except:
        mtype=mst(a)
        if mtype == "private":
            spm(qui(a),"命令或参数有误")
        elif mtype == "group":
            sgm(qgi(a),"命令或参数有误")
        # print("命令或参数有误")

def dodelall(a,cs):
    try:
        com.pop(cs)
        xh(com)
        mtype=mst(a)
        if mtype == "private":
            spm(qui(a),"关键词 "+cs+" 删除成功")
        elif mtype == "group":
            sgm(qgi(a),"关键词 "+cs+" 删除成功")
        # print(com[gjc])
    except:
        mtype=mst(a)
        if mtype == "private":
            spm(qui(a),"没有这个关键词，你在删空气？")
        elif mtype == "group":
            sgm(qgi(a),"没有这个关键词，你在删空气？")

def dolist(a,cs):
    try:
        lis=com[cs]
        ans=""
        for i in lis:
            ans+=i
            ans+="\n"

        mtype=mst(a)
        if mtype == "private":
            spm(qui(a),"关键词 "+cs+" 回答列表：\n"+ans)
        elif mtype == "group":
            sgm(qgi(a),"关键词 "+cs+" 回答列表：\n"+ans)
            # print("关键词 "+cs+" 回答列表：\n"+ans)
    except:
        mtype=mst(a)
        if mtype == "private":
            spm(qui(a),"没有这个关键词，你在列举空气？")
        elif mtype == "group":
            sgm(qgi(a),"没有这个关键词，你在列举空气？")


