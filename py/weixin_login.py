#
#time=18.5.20
#_auther_=lixiaojie

from  wxpy import *
import string

login = Bot(cache_path = True)

name = '郭华'

doc = 'hello,my name is xiaojie'

friends =login.friends(update=False)   #获取更新好友

friend_zou = ensure_one(login.search(name))

friend_zou.send(doc)

tuling = Tuling(api_key='b397ed26a13c42db995effe99853941e')

@login.register(friend_zou)

def reply_my_friend(msg):
    tuling.do_reply(msg)

embed()