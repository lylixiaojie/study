# -*- coding:utf-8 -*-
#__authon__==lixiaojie
#本文件用来实现修改使用jenkens打包的名字

import ftplib
import os


#命名
host = 'ftp.haocai.sz'   #ftp地址
username = 'ftpserver'    #用户名
passwd = 'haocai888'      #用户密码
mulu = '/Releases/Android/'
mulu_qz_market_97 = '/Releases/Android/quanzhong/market/97/'
name_qudao=['quanzhong/','lianzhong/','lianzhongcai/']
name_package=['info/','market/','office/']
name_icon=['97/','oldicon/']



#连接登陆ftp
def ftp_login():
    try:
        link_ftp = ftplib.FTP(host)
        link_ftp.login(username, passwd)
        return link_ftp
    except IOError:
        print("can't login")


def ftp_rename(oldname, newname):
    try:
        ftp_login().rename(oldname, newname)
        print('update' + oldname)
    except:
        print('')






ftp_login()
ftp_oldname = input('please input oldname:')
#ftp_oldname='new.txt'
ftp_newname= input('please input newname:')

for x in range(0, len(name_qudao)):
    for y in range(0, len(name_package)):
        for z in range(0, len(name_icon)):
            ftp_oldname_user = mulu + name_qudao[x] + name_package[y] + name_icon[z] + ftp_oldname
            ftp_newname_user = mulu + name_qudao[x] + name_package[y] + name_icon[z] + ftp_newname
            ftp_rename(ftp_oldname_user, ftp_newname_user)

ftp_login().quit()