#__author__=lixiaojie
# 代码用来实现url生成二维码
#

import qrcode

def make_qrcode():
    input_print=input("please input you want:")
    img = qrcode.make(input_print)
    img.save('E:/a.png')

make_qrcode()


