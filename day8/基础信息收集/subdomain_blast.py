import difflib
import hashlib
import json
import dns.resolver
import requests
from bs4 import BeautifulSoup

from foundation_info import FoundationInfo


class SubdomainBlast():
    '''
    测试泛解析
    '''

    # taobao.com存在
    def __init__(self):
        self.domain1 = 'nianqijiduannianqibusui'
        self.domain2 = 'nianqijijuejuezhijiwu'

    def get_analysis(self, domain):
        try:
            # 使用 dnspython DNS查询某个子域名的 A 记录--查询不到会报错
            # 使用 requests 向组合后的子域名发起 HTTP GET 请求--请求不到会报错
            # 报错就说明没有泛解析
            dns.resolver.resolve(self.domain1 + '.' + domain, rdtype='A')
            print(1313)
            dns.resolver.resolve(self.domain2 + '.' + domain, rdtype='A')
            res1 = requests.get('http://' + self.domain1 + '.' + domain)
            res2 = requests.get('http://' + self.domain2 + '.' + domain)
            # 使用 difflib.SequenceMatcher 计算内容的相似度比率
            check_ab = difflib.SequenceMatcher(None, res1.text, res2.text).quick_ratio()
            if check_ab >= 0.90:
                return True
        except:
            return False

    """
        获取IP地址归属
        """

    def get_ip_address(self, ip):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
        }
        res = requests.get(f'https://www.ipshudi.com/{ip}.htm', headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        res = soup.find_all(class_='ft')
        for ft in res:
            find_span = ft.find_all('span')
            return find_span[1].text

    """
    指纹识别
    """

    # 测试网站：http://swiftcolud.cn/about.html
    def fingerscan(self, domain):
        cms = open('cms.json', 'r', encoding="utf-8").read()
        for c in json.loads(cms)['data']:
            # 先判断re
            if c['re'] == '':
                # 得到文件的MD5值
                res = requests.get('http://' + domain + c['url']).text
                md5 = hashlib.md5()
                md5.update(res.encode('utf-8'))
                # 判断和文件
                if md5.hexdigest() == c['md5']:
                    return (c['name'])
            else:
                res = requests.get('http://' + domain + c['url']).text
                if res.find(c['re']) != -1:
                    return (c['name'])

    '''
    子域名爆破
    '''

    # domain: 成功爆破：ke-scm.com 泛解析：taobao.com isuperone.com(404统一)
    def sub_domain(self, domain):
        is_analysis = self.get_analysis(domain)
        if is_analysis is False:
            domain_list = []
            # 循环爆破域名
            for s_domain in open('domain.txt', 'r').readlines():
                # 去除每行末尾的换行符 \n
                s_domain = s_domain.replace('\n', '')
                try:
                    # 域名的 A 记录，有就下一步得到对应的ip，没有会报错，爆破下一个
                    query_res = dns.resolver.resolve(s_domain + '.' + domain, rdtype='A')
                    # 判断CDN
                    found = FoundationInfo()
                    res = found.get_cdn(s_domain + '.' + domain)
                    if res is True:
                        # 存在CDN，直接返回域名
                        finger = self.fingerscan(s_domain + '.' + domain)
                        domain_list.append(s_domain + '.' + domain + '>>>' + finger)
                    else:
                        # 遍历 DNS 返回的响应答案部分（看不懂），这样获得域名对应的ip
                        print(666)
                        finger = self.fingerscan(s_domain + '.' + domain)
                        print(666)
                        for query_item in query_res.response.answer:
                            for item in query_item.items:
                                ipa = self.get_ip_address(str(item))
                                domain_list.append(s_domain + '.' + domain + '>>>' + str(item) + '>>>' + ipa + '>>>' + finger)
                                # print(666)
                    # 获得ip地址归属
                    # self.get_ip_address(s_domain +'.'+domain)
                except:
                    pass
            return domain_list
        else:
            return '该域名存在泛解析'


# 主程序入口
if __name__ == '__main__':
    subdomain = SubdomainBlast()
    res = subdomain.sub_domain("cn")
    print(res)

    # 判断文件的url值
    # md5 = hashlib.md5()
    # md5.update(requests.get('http://swiftcolud.cn/DM-static/assets/cssjs/DM.js?v=').text.encode('utf-8'))
    # print(md5.hexdigest())
