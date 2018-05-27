# -*- coding:utf-8 -*-
#__authon__==lixiaojie
#本文件用来实现修改使用jenkens打包的名字

import ftplib


#命名
host = 'ftp.haocai.sz'
username = 'ftpserver'
passwd = 'haocai888'
mulu = '/Releases/Android'
mulu_qz_market_97 = '/Releases/Android/quanzhong/market/97'

#连接登陆ftp
def ftp_login():
    link_ftp = ftplib.FTP(host)
    link_ftp.login(username, passwd)
    link_ftp.cwd(mulu_qz_market_97)
    return link_ftp
def ftp_find_quanzhong_market_97():
    ftp_path_quanzhong_market_97 = ftp_login().dir()
    print(ftp_path_quanzhong_market_97)


def ftp_rename(oldname, newname):
    ftp_path_rename = ftp_login().rename(oldname, newname)
    return ftp_path_rename


ftp_login()
ftp_find_quanzhong_market_97()
#oldname = input('please input oldname')
ftp_oldname='new.txt'
ftp_newname= input('please input newname:')
ftp_rename(ftp_oldname, ftp_newname)




ftp_login().quit()