class Screen(object):
    @property
    def width1(self):
        return self.width

    @property
    def height1(self):
        return self.height

    @property
    def resolution1(self):
        self.resolution = '解决中....'
        return self.resolution

    @width1.setter
    def width1(self,value):
        self.width = value

    @height1.setter
    def height1(self,value):
        self.height = value

class aaa(object):
    def aaa(self):
        print('aaatest')

class aaa1(object):
    def aaa(self):
        print('bbbtest')

class testaaa(aaa1,aaa):
    def hahaha(self):
        print('hahahahaha')

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器 a， b
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值


class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
foo('0')


'''

for n in Fib():
    print(n)


test1 = testaaa()
test1.aaa()



s = Screen()
s.height1 = 20000
print('高：',s.height1)
s.width1 = 200
print('高：',s.width)
#s.resolution1 = 200
print('方法：',s.resolution1)
'''




