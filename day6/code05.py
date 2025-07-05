import requests
from bs4 import BeautifulSoup

res = requests.get('https://spiderbuf.cn/web-scraping-practice/requests-lxml-for-scraping-beginner')
sou = BeautifulSoup(res.text, 'html.parser')
all_div = sou.find('div',class_='adsbygoogle')
print(all_div)
# print(all_div)
# for div in all_div:
#     print(div)
#     print('-------')