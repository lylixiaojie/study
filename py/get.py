#coding=utf-8

import json
import requests
import random
import time

#随机数的最小和最大
count=1000000000000000
count_end=9999999999999999

#执行次数
number=10000
url_pojie='http://ebookdomainry.pep.com.cn/api'

#生成key
def key():
    keyjihuo=random.randint(count,count_end)
    key_j=str(keyjihuo)
    tou="02"
    key_jh=tou+key_j
    return key_jh

#json
def json_p():
    json_pojie=json.dumps({"data":{"book_id":"10001","user_id":2480427,"activation_code":key()},"action":"activateBook"})
    return json_pojie

#请求头
headers={'Content-Length':'107',
'Content-Type':'text/plain;charset=UTF-8',
'Host':'ebookdomainry.pep.com.cn',
'Connection':'Keep-Alive'}


#请求函数
def go_do():
    do=requests.post(url_pojie, data=json_p(), headers=headers)
    print(json_p())
    print("this is status:")
    print(do.status_code)
    print("this is text:")
    print(do.text)
    return do

#执行


for i in range(number):
    print (i)
    a=go_do().text

    #print("a:"+ a[20:24])
    b=a[20:24]
    time.sleep(3)
    #print("b:"+b)
    if b!="7002":
        break


