import requests

url = 'https://spiderbuf.cn/web-scraping-practice/requests-lxml-for-scraping-beginner'
res = requests.get(url=url).content
# 能解决乱码
# res = requests.get(url=url).text
print(res)