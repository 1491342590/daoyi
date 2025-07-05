def poc(url,bugtype):

    if url == '':
        print('URL不能为空')

    if bugtype == 'shiro':
        print(f'shiro漏洞  URL：{url}')

    if bugtype == 'dahua':
        print(f'dahua漏洞  URL：{url}')

    if bugtype == 'thinkphp':
        print(f'thinkphp漏洞  URL：{url}')

msg =input('请输入URL 指定漏洞 空格分割：').split(' ')

poc(url = msg[0].lower(),bugtype=msg[1].lower())