from urllib import request

with request.urlopen("https://www.baidu.com/s?wd=urllib&rsv_spt=1&rsv_iqid=0xc38d9b150000f3cb&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=2&rsv_n=2&rsv_sug1=1&rsv_sug7=100&rsv_sug2=0&inputT=1519&rsv_sug4=1699") as u:
	data=u.read()
	print ("Staus:",u.status,u.reason)
	#for k,v in u.getheaders():
		#print("%s:%s "%(k,v))
	print ("data",data)