import re


line = 'http://www.runoob.com/python/python-reg-expressions.html'

zhengze = 'www(.*?)com'

a = re.search(zhengze,line,re.M)
if a:
    print(a.group())
    print(a.group(1))

else:
   print ("No a")