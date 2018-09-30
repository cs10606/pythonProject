list1 = ['key1','key2','key3']

list2 = ['1','2','3']

r=dict(zip(list1,list2))
print(type(r))
print(r)

x = [1, 2, 3]

y = [4, 5, 6]

z = [7, 8, 9]

xyz = tuple(zip(x, y, z))

print (xyz)

import requests

resp = requests.get(url)
cookies = resp.cookies
print('; '.join(['='.join(item) for item in cookies.items()]))

requests.
