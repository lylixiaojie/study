#coding=utf-8
#全中彩票app签到

import requests
import json
import ssl
import re

#手机号
mobile='18810722283'



#密码
passwd='95025c8ffea5f4876cc499823aefbb38'

#登陆的json
def json_p():
    json_pojie=json.dumps({"mobile":mobile,"password":passwd,"av":"2.6.1","jv":"0042","d":"Dalvik/2.1.0 (Linux; U; Android 8.0.0; MI 6 MIUI/8.4.26)","c":"LZ_testA","tid":"dfcJGgThfBE","m":"MI 6","os":"android","ts":1525357136041,"net":"WIFI"})
    return json_pojie

#签到的json
def json_qiandao():
    json_qian=json.dumps({"sessionKey":sessionkey.group(1),"av":"2.6.1","jv":"0042","d":"Dalvik/2.1.0 (Linux; U; Android 8.0.0; MI 6 MIUI/8.4.26)","c":"LZ_testA","tid":"fDdhBm_tMjU","m":"MI 6","os":"android","ts":1525617163969,"net":"WIFI","uid":uid.group(1)})
    return json_qian

#app通用请求头
headers={'accept': 'application/json, text/plain, */*',
'Content-Type': 'application/json;charset=utf-8',
'Content-Length': '251',
'Host': 'service.quancp.com',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'User-Agent': 'okhttp/3.4.1'}

#登陆的url地址
url_denglu="https://service.quancp.com/v1/login"

#签到的url地址
url_qiandao="https://activity.quancp.com/v1/doSign"



#登陆接口
def go_do():
    do = requests.post(url_denglu, data=json_p(), headers=headers,verify=False)
    print(do.text)
    return do

#签到接口
def qiandao():
    qian = requests.post(url_qiandao, data=json_qiandao(), headers=headers,verify=False)
    return qian

#sessionkey的正则表达式
zhengze_session='sessionKey":"(.+?)"'

#用户id的正则表达式
zhengze_uid='"userId":"(.+?)",'

#调用登陆函数
a = go_do()
#通过登陆接口获取sessionkey的正则表达式
sessionkey = re.search(zhengze_session,a.text,re.M)

#通过登陆接口获取用户的正则表达式

uid = re.search(zhengze_uid,a.text,re.M)
print(sessionkey.group(1))
print(uid.group(1))
print(a.text)

#调用签到接口
b = qiandao()
print(b.text)

