#李小杰 18.3.11
#python
#这个程序是用来学习函数

x=0

#函数是用来输入一个整数，然后判断整数是正负或这0
def daxiao(x):
	x=input("please input one number:")
	x=int(x)
	if x>0:
		print ("x is 正，x is :",x)
	elif x==0:
		print("x is 0")
	else: 
		print ("x is 负,x is :",x)
	
#调用函数	
daxiao(x)
	
