import difflib
import dns.resolver
import requests


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
            # 使用 dnspython 查询某个子域名的 A 记录--查询不到会报错
            # 使用 requests 向组合后的子域名发起 HTTP GET 请求--请求不到会报错
            dns.resolver.resolve(self.domain1 + '.' + domain, rdtype='A')
            dns.resolver.resolve(self.domain2 + '.' + domain, rdtype='A')
            res1 = requests.get('http://' + self.domain1 + '.' + domain)
            res2 = requests.get('http://' + self.domain2 + '.' + domain)
            check_ab = difflib.SequenceMatcher(None, res1.text, res2.text).quick_ratio()
            if check_ab >= 0.90:
                return True
        except:
            return False

    '''
    子域名爆破
    '''
    # domain: 成功爆破：wgpsec.org 泛解析：taobao.com
    def sub_domain(self, domain):
        is_analysis = self.get_analysis(domain)
        if is_analysis == False:
            for domain_a in open('domain.txt','r').readlines():
                domain_a = domain_a.replace('\n','')
                try:
                    dns.resolver.resolve(domain_a +'.'+domain,rdtype='A')
                    print(domain_a +'.'+domain)
                except:
                    pass
        else:
            print('该域名存在泛解析')

# 主程序入口
if __name__ == '__main__':
    sub = SubdomainBlast()
    sub.sub_domain('tobao.com')
