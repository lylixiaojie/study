# -*- coding: UTF-8 -*-

from urllib import request, parse
import json

li_json=[ { "data" : { "book_id" : "10001" , "user_id" : 2480427 , "activation_code":"987369850806402823" } , "action":"activateBook" } ]

#data = [{ 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

req_json = json.dumps(li_json)
req_post = req_json.encode('utf-8')


login_data = parse.urlencode (req_post)

req = request.Request(url='http://ebookdomainry.pep.com.cn/api')
req.add_header('Content-Length', 109)
req.add_header('Content-Type', 'text/plain; charset=UTF-8')
req.add_header('Host', 'ebookdomainry.pep.com.cn')
req.add_header('Connection', 'Keep-Alive')


with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))



