class Student():
    def __init__(self):
        print('初始化内容：——————1313——————')
        self.name = '张三'
        self.nianl = 19

    def tw(self):
        print(self.name, '会跳舞')

    def cg(self):
        print(self.name, '会唱歌')

stu = Student()
print(stu.name)
stu.tw()