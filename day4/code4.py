import re

# phone = '127.0.0.1'
# print(re.match('\d{1,4}\.\d{1,4}\.\d{1,4}.\d{1,4}',phone).group(0))


phone = 'http://www.baidu.com'
print(re.match('http.{1,3}//.*',phone).group(0))
