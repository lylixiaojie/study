#time 18.5.20
#_auther=lixiaojie

import requests

url='http://www.lixj.top'

def go():
    do=requests.get(url)
    return do


for i in range(1,100000):
    go()

