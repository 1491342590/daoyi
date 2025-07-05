class Student():
    __name = '张三'
    idcard = '1323214124adswq'
    def __tw(self):
        print(self.__name, '会跳舞')

    def cg(self):
        print(self.__name, '会唱歌')
        self.__tw()

stu = Student()
stu.cg()