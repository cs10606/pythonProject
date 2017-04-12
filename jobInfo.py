import requests
import json
import re

url1 = 'https://logintest.fulu.com/api/loginv2/authenticate1?username=jfstest1&password=OMA1HIJrDET%2fNrZFVxZYs1XiRuGkHXL%2f1IWhieh0m6X2JuA%2fCEhif73%2fmx0Uen7DrmYUeyPzyRrty3MHhF386A%3d%3d&verifycode=&client_id=88888889&from=sup&type=on&redirect_uri=http%3a%2f%2f121.40.209.239%3a15001%2factive.html&callback=callback&_=1491814552608'#登陆地址
url2 ='http://121.40.209.239:15001/accountservice.svc/active'
url3 = "http://121.40.209.239:15001/ProductService.svc/GetMyKamenNetProductList"#需要登陆才能访问的地址
data2={"PageNumber":"1","PageSize":"15"}
session = requests.Session()
res1 = session.get(url1)



res1.encoding='utf-8'

data=res1.text
#print(type(data))
#print(data)
aa= data[9:-1]
#print(aa)
result = json.loads(aa)
print(result)

headers = {'Content-Type': 'application/json'}
Data1='"'+result["Data"]+'"'
res2=session.post(url2,data=Data1,headers=headers)


print(res2.url)
print(res2.status_code)
#print(res2.cookies)
res3=session.post(url3,data=json.dumps(data2))
print(res3.status_code)
print(res3.json())



