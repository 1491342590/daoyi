st = '1214wefew'
print(st[-2:])

st1 = 'http://baidu.com'
if st1.find('https') != -1:
    print('https协议')
else:
    print('http协议')

st2 = st1.replace('http','https')
print(st2)

st3 = st1.split('://')
print(st3)

li = ['1','2','3','4','5']
str1 = ' '.join(li)
print(str1)
