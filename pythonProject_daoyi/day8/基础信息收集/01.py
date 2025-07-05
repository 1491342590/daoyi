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
        iscdn = True
        data = res.xpath('/html/body/div[3]/text()')
        if data[0].find('不属于CDN云加速') != -1:
            print('存在CDN')
        else:
            iscdn = False
            print('不属于CDN')
        return iscdn

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

found = FoundationInfo()
res = found.fancha('iredteam.cn')
print(res)