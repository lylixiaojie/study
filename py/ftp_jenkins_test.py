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
    else:
        print("I don't know")

def ftp_rename(oldname, newname):
    for x in range(0,len(name_qudao)):
        for y in range(0,len(name_package)):
            for z in range(0,len(name_icon)):
                ftp_oldname = mulu + name_qudao[x] + name_package[y] + name_icon[z] + oldname
                ftp_newname = mulu + name_qudao[x] + name_package[y] + name_icon[z] + newname
                try:
                    ftp_path = ftp_login().rename(ftp_oldname, ftp_newname)
                    return ftp_path
                except IOError as error:
                    print("can't update")
                    print(error)
                    print(ftp_oldname)
                    continue
                else:
                    print("I don't know")
                    print(ftp_oldname)
                    continue
                #z=z+1
            #y=y+1
        #x=x+1


ftp_login()
ftp_oldname = input('please input oldname:')
#ftp_oldname='new.txt'
ftp_newname= input('please input newname:')
ftp_rename(ftp_oldname, ftp_newname)



ftp_login().quit()