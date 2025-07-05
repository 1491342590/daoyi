class shifu():
    jineng = '渗透测试'
    def work(self):
        print('做web渗透测试')

class tudi(shifu):
    def work(self):
        print('师傅会代码审计')

td = tudi()
td.work()