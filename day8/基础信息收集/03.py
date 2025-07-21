import base64
import difflib
import hashlib
import json
import threading
import argparse
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

    # 指纹扫描
    def fingerscan(self, url):
        cms = open('cms.json', 'r', encoding='utf-8').read()
        for c in json.loads(cms)['data']:
            if c['re'] == '':
                res = requests.get(url + c['url']).text
                md5 = hashlib.md5()
                md5.update(res.encode('utf-8'))
                if md5.hexdigest() == c['md5']:
                    return c['name']
            else:
                res = requests.get(url + c['url']).text
                if res.find('aspcms') != -1:
                    return c['name']
        return None

    # 子域名爆破
    def sub_domain(self, domain):
        is_analysis = self.get_analysis(domain)
        if is_analysis is True:
            domain_list = []
            for sdomain in open('domains.txt', 'r').readlines():
                sdomain = sdomain.replace('\n', '')
                try:
                    query_res = dns.resolver.resolve(sdomain + '.' + domain, rdtype='A')
                    fing = self.fingerscan('http://'+domain)
                    found = FoundationInfo()
                    res = found.get_cdn(sdomain + '.' + domain)
                    if res is True:
                        print(sdomain + '.' + domain)
                        domain_list.append(sdomain + '.' + domain+">>>"+fing)
                    else:
                        for query_item in query_res.response.answer:
                            for item in query_item.items:
                                ipg = self.get_ip_address(item)
                                # print(sdomain + '.' + domain+'>>>'+str(item)+'>>>'+ipg)
                                domain_list.append(sdomain + '.' + domain+'>>>'+str(item)+'>>>'+str(ipg)+">>>"+fing)
                except:
                    pass
            return domain_list
        else:
            return '该域名存在泛解析'


class DirScan():
    def run(self,url,dir_dict):
        dic_list = []
        dics = open(dir_dict,'r').readlines()
        for dic in dics:
            res = requests.get(url+dic.replace('\n',''),verify=False).status_code
            if res != 404:
                dic_list.append(url+dic.replace('\n',''))
                print(url+dic.replace('\n',''))
        return dic_list



class Fofa_Api():
    def get_data(self,keyword):
        keyword = base64.b64encode(keyword.encode)
        url = f'https://fofa.info/api/v1/search/all?&key=your_key&qbase64={keyword}'
        res = requests.get(url).json()
        print(res['results'])


parse = argparse.ArgumentParser(
    prog='信息收集工具'
)
parse.add_argument('-u','--url',help='要收集的域名')
parse.add_argument('-dir','--DirScan',action='store_true',required=False,help='是否扫描目录')
parse.add_argument('-foun','--FoundationInfo',action='store_true',required=False,help='是否收集基础信息')
parse.add_argument('-dict','--dirdict',required=False,help='目录字典')
args = parse.parse_args()
print(args.DirScan)
print(args.url)
print(args.FoundationInfo)

if args.DirScan:
    if args.dirdict is False:
        print('需要设置字典')
    dirscan = DirScan()
    th = threading.Thread(target=dirscan.run,args=[args.url,args.dirdict]).start()
    