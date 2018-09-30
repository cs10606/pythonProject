import requests
import json

r=requests.get("http://www.baidu.com")
print(r.status_code)
print(r.url)
print(r.text)
r1=json.loads(r.text)
print(r.content)
print(r.cookies)
I = ['iplaypython', [1, 2, 3], {'name':'xiaoming'}]
encoded_json = json.dumps(I)
print (type(encoded_json))
print (repr(I))
print (json.dumps(encoded_json))
decode_json = json.loads(encoded_json)
print (type(decode_json)) #查看一下解码后的对象类型
print (decode_json) #输出结果