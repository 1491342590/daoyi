class dongwu():
    def eat(self):
        print('动物要吃东西')

class Dog():
    def eat(self):
        print('狗要吃肉')

class Person():
    def eat(self):
        print('人要吃饭')

def fun(cls):
    cls.eat()

fun(Person())