import requests
import whois
from bs4 import BeautifulSoup
from urllib.parse import quote


class FoundationInfo():
    '''
    CND信息查询
    '''
    # 通过多个直接返回ip的接口来判断是否存在cdn
    # 借用接口的网站：https://uutool.cn/cdn-check/
    # 测试：totolgroup.cn —— 无
    # gettexttools.com —— 有
    # 输入域名：domain
    def get_cdn(self, domain):
        urls = [
            f"https://ips-app-nnrrjaztiz.cn-hangzhou.fcapp.run/?domain={domain}/",
            f"https://ips-web-fnrrjazpxz.cn-shanghai.fcapp.run/?domain={domain}/",
            f"https://ips-app-nnrrjaztiz.cn-qingdao.fcapp.run/?domain={domain}/",
            f"https://ips-app-nnrrjaztiz.cn-beijing.fcapp.run/?domain={domain}/",
            f"https://ips-app-vrdhcyxprn.cn-zhangjiakou.fcapp.run/?domain={domain}/",
            f"https://ips-app-vrdhcyxprn.cn-huhehaote.fcapp.run/?domain={domain}/",
            f"https://ips-app-nnrrqmtriz.cn-shenzhen.fcapp.run/?domain={domain}/",
            f"https://ips-app-vrdhcyxprn.cn-chengdu.fcapp.run/?domain={domain}/",
            f"https://ips-app-nnrrjaztiz.cn-hongkong.fcapp.run/?domain={domain}/",
            f"https://ips-app-vrdhcyxprn.ap-northeast-1.fcapp.run/?domain={domain}/",
            f"https://ips-app-vrdhcyxprn.ap-northeast-2.fcapp.run/?domain={domain}/"
        ]
        #
        ip_addresses = []
        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                # 返回单个/多个ip
                ip_address = response.text.strip().split(',')
                # 没有相同的ip则添加
                for ip in ip_address:
                    if ip not in ip_addresses:
                        ip_addresses.append(ip)
        # print(ip_addresses)
        # 只有一个相同的ip时
        if len(ip_addresses) == 1:
            print(f"{domain} 无cdn")
        else:
            print(f"{domain} 有cdn")


    '''
    whois信息查询
    '''
    # 域名：tjacucampus.unipus.cn
    def get_whois(self, domain):
        res = whois.whois(domain)
        print(res)
        # json格式，要啥  取啥
        # print(res['name'])

        # 邮箱
        print(res['emails'])
        # 注册人
        print(res['name'])


    '''
    备案信息查询
    '''
    # domain：ciptc-sz.com
    def get_icp(self, domain):
        headers = {
            'Cookie': '.AspNetCore.Antiforgery.OGq99nrNx5I=CfDJ8KZctS8FUKZJlMA3zPFGIiO9C-xasidLrGTwEERFUrIB7NIG_cgzIyaftofEpM0Ix3gtd-hMZTqxsFCLuTmR2m9i-sB2wcgbVulumOfkB5A_sNWJvoGjqdWJMKgYPZ3fkyJbDBxHxeVg3WacbEcG3qw; __51vcke__JfvlrnUmvss1wiTZ=463a3951-29af-595d-a655-bd95ca648fcb; __51vuft__JfvlrnUmvss1wiTZ=1750322450874; SL_G_WPT_TO=zh; machine_str=b8a0f12b-ac28-4533-8916-f0bf7983ecdc; acw_tc=0aef815517503274087565425e00742ac7b5f775fd7a160e46665f6a6b63a0; __51uvsct__JfvlrnUmvss1wiTZ=2; __vtins__JfvlrnUmvss1wiTZ=%7B%22sid%22%3A%20%227a7277d0-235e-5181-bbb0-49e7d53e2a8f%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%201290381%2C%20%22dr%22%3A%201027655%2C%20%22expires%22%3A%201750330500788%2C%20%22ct%22%3A%201750328700788%7D'
        }
        # 网站：https://www.beianx.cn/search
        res = requests.get(url=f"https://www.beianx.cn/search/{quote(domain)}", headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        datas = soup.find_all(class_='align-middle')
        print(datas[0].text.strip())
        print(datas[1].text.strip())
        print(datas)


    '''
    备案号反查域名
    '''
    # 备案号：京ICP备17003970号
    def get_icp_domain(self, domain):
        headers = {
            'Cookie': '.AspNetCore.Antiforgery.OGq99nrNx5I=CfDJ8KZctS8FUKZJlMA3zPFGIiO9C-xasidLrGTwEERFUrIB7NIG_cgzIyaftofEpM0Ix3gtd-hMZTqxsFCLuTmR2m9i-sB2wcgbVulumOfkB5A_sNWJvoGjqdWJMKgYPZ3fkyJbDBxHxeVg3WacbEcG3qw; __51vcke__JfvlrnUmvss1wiTZ=463a3951-29af-595d-a655-bd95ca648fcb; __51vuft__JfvlrnUmvss1wiTZ=1750322450874; SL_G_WPT_TO=zh; machine_str=b8a0f12b-ac28-4533-8916-f0bf7983ecdc; acw_tc=0aef815517503274087565425e00742ac7b5f775fd7a160e46665f6a6b63a0; __51uvsct__JfvlrnUmvss1wiTZ=2; __vtins__JfvlrnUmvss1wiTZ=%7B%22sid%22%3A%20%227a7277d0-235e-5181-bbb0-49e7d53e2a8f%22%2C%20%22vd%22%3A%203%2C%20%22stt%22%3A%201290381%2C%20%22dr%22%3A%201027655%2C%20%22expires%22%3A%201750330500788%2C%20%22ct%22%3A%201750328700788%7D'
        }
        # 网站：https://www.beianx.cn/search
        res = requests.get(url=f"https://www.beianx.cn/search/{quote(domain)}", headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        res = soup.find_all('tr')
        for i in res:
            finda = i.find_all('a')
            for a in finda:
                if a['href'].find('seo') != -1:
                    print(a.text)

if __name__ == "__main__":
    domain = input("请输入要检测的域名：\n")
    found = FoundationInfo()
    found.get_whois(domain)
