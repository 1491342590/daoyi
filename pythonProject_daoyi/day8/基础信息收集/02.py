import difflib
import json

import dns.resolver
import requests
from lxml import etree
from bs4 import BeautifulSoup
import whois
from urllib.parse import quote


# 基础信息收集模块
class FoundationInfo():
    # 判断是否是CDN   domain：域名
    def get_cdn(self, domain):
        data = {
            'type': 'host',
            'host': domain,
            'hfUrl': domain,
            't': '电信, 联通, 移动'
        }
        res = requests.post(url=f'https://cdn.chinaz.com/search/?host={domain}', data=data)
        res = etree.HTML(res.text)
        data = res.xpath('/html/body/div[3]/text()')
        if data[0].find('使用CDN') != -1:
            return True
        if data[0].find('不属于CDN云加速') != -1:
            return True
        else:
            return False

    # 获取whois信息   domain：域名
    def get_whois(self, domain):
        res = whois.whois(domain)
        email = res['emails']
        return res

    # 获取IPC备案号
    def get_ipc(self, domain, type):
        datlist = []
        # 备案号反查域名
        if type == 'ipctodomain':
            res = requests.get(url=f'https://www.beianx.cn/search/{quote(domain)}')
            soup = BeautifulSoup(res.text, 'html.parser')
            res = soup.find_all('tr')
            datlist = []
            for i in res:
                finda = i.find_all('a')
                for a in finda:
                    if a['href'].find('seo') != -1:
                        datlist.append(a.text)

        else:
            # 域名查询备案号
            res = requests.get(url=f'https://www.beianx.cn/search/{domain}')
            soup = BeautifulSoup(res.text, 'html.parser')
            datas = soup.find_all(class_='align-middle')
            dname = datas[1].text.replace('\n', '')
            datlist.append(dname)
            xingz = datas[2].text.replace(' ', '').replace('\n', '')
            datlist.append(xingz)
            ipc_id = datas[3].text.replace(' ', '').replace('\n', '')
            datlist.append(ipc_id)
        return datlist

    # 查询注册人
    def fancha(self, domain):
        res = self.get_whois(domain)
        return str(res['name']).encode('utf-8').decode()


class SubdomainExplosion():
    def __init__(self):
        self.domain1 = 'asfsdgdfsgfasdfdsdfs'
        self.domain2 = 'yuiopiuytgvbnmkjhghfghfjb'

    # 测试泛解析
    def get_analysis(self, domain):
        try:
            dns.resolver.resolve(self.domain1 + domain, rdtype='A')
            dns.resolver.resolve(self.domain2 + domain, rdtype='A')
            res1 = requests.get('http://' + self.domain1 + domain)
            res2 = requests.get('http://' + self.domain2 + domain)
            check_ana = difflib.SequenceMatcher(None, res1.text, res2.text).quick_ratio()
            if check_ana >= 0.90:
                print('存在泛解析')
            else:
                res = input('可能存在泛解析，是否继续爆破 Yes No：')
                if res == 'Yes':
                    return True
                else:
                    return False
        except:
            return True

    # 获取IP地址归属
    def get_ip_address(self, domain):
        res = requests.get(f'http://ip-api.com/json/{domain}?lang=zh-CN')
        return res.json()['country']+res.json()['regionName'], res.json()['city']

    # 子域名爆破
    def sub_domain(self, domain):
        is_analysis = self.get_analysis(domain)
        if is_analysis is True:
            domain_list = []
            for sdomain in open('domains.txt', 'r').readlines():
                sdomain = sdomain.replace('\n', '')
                try:
                    query_res = dns.resolver.resolve(sdomain + '.' + domain, rdtype='A')
                    found = FoundationInfo()
                    res = found.get_cdn(sdomain + '.' + domain)
                    if res is True:
                        print(sdomain + '.' + domain)
                        domain_list.append(sdomain + '.' + domain)
                    else:
                        for query_item in query_res.response.answer:
                            for item in query_item.items:
                                ipg = self.get_ip_address(item)
                                # print(sdomain + '.' + domain+'>>>'+str(item)+'>>>'+ipg)
                                domain_list.append(sdomain + '.' + domain+'>>>'+str(item)+'>>>'+str(ipg))
                except:
                    pass
            return domain_list
        else:
            return '该域名存在泛解析'

    def what_cms(self,domain):
        zidian  = open('zidian.json','r',encoding='utf-8').read()
        for i in json.loads(zidian)['cmsdata']:
            res = requests.get(domain).text
            print(res)
            if res.find(i['text']) != -1:
                print(i['cmsname'])

# found = FoundationInfo()
# res = found.get_cdn('cip.cc')
# print(res)

sub = SubdomainExplosion()
# res = sub.get_ip_address('120.79.199.196')
res = sub.what_cms('http://120.79.199.196')
# if type(res) is list:
#     for i in res:
#         print(i)
# else:
#     print(res)