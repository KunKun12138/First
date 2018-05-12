#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' a test module '
__author__ = 'liuyi'

import math
import sys

from functools import reduce
import functools

def log(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('Begin %s %s:' % (text, func.__name__))
            out1 = func(*args, **kw)
            print('End %s %s:' % (text, func.__name__))
            return out1
        return wrapper
    return decorator

def Multiple_ReturnValue(score_thisyear,score_lsatyear):
    #score_thisyear = eval(input('今年的成绩'))
    #score_lsatyear = eval(input('去年的成绩'))
    if not isinstance(score_thisyear,(int,float)):
        raise TypeError('错误的参数类型')
    difference = score_thisyear - score_lsatyear
    improvePrecent = (difference/ score_lsatyear) * 100
    improvePrecent_abs = abs((difference / score_lsatyear) * 100)
    if (improvePrecent > 0):
        print('今年的成绩比去年提升：%.1f%%' % improvePrecent_abs)
        return improvePrecent,difference
    else:
        print('今年的成绩比去年下降：%.1f%%' % improvePrecent_abs)
        return improvePrecent, difference

def jiefangcheng(a,b,c,*kw):
    print(kw)
    if(a!=0):
        e = b * b - 4 * a * c
        if(e >= 0):
            x1 = (-b + math.sqrt(e))/2/a
            x2 = (-b - math.sqrt(e))/2/a
            if(x1 == x2):
                return x1
            else:
                return x1,x2
        else:
            withoutAnswer = '此题无解1,下一题：'
            a = eval(input('a:'))
            b = eval(input('b:'))
            c = eval(input('c:'))
            jiefangcheng(a, b, c)
    elif(a == 0):
        if(b != 0):
            x1 = -b/c
            return x1
        else:
            withoutAnswer = '此题无解2'
            return withoutAnswer

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum1 = sum + n * n
    return sum1

def Fibonacci(maxnum):
    a,b,c = 0,1,1
    print(b)
    while(c < maxnum):
        e = a + b
        yield (e)
        a = b
        b = e
        c = c + 1
    return 'done'

def YangHuiSanJiao(HS):
    L1,L2,hangshu= [1],[1],1
    while(hangshu <= HS):
        yield L2
        lieshu ,hangshu,L1,L2= 0,hangshu + 1,L2,[]
        while(lieshu < hangshu):
            L2.append(1 if(lieshu == 0 or lieshu == hangshu -1) else L1[lieshu] + L1[lieshu - 1])
            lieshu = lieshu + 1

#将首字母装换成大写，其他字母小写
def TheFirstWordCapitalize(str1):
    s= str1.capitalize()
    return s


def do_reduce_prod(a,b):
    return a * b

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

#过略掉非回数
#定义回数
def IsHuiShu(n):
    L = []
    while (n / 10 >= 1):
        c = n%10
        L.append( int(c))
        n = n / 10
    L.append(int(n))
    a = 0
    b = 0 #用于判断对弈位数是否相等
    while (a < math.ceil(L.__len__()/2)):
        if (L[a] == L[L.__len__() - a -1] and a != L.__len__() - a -1):
            b = 1
            a = a + 1
        else:
            b = 0
            a = a + 1
            return b == 1
    return b == 1

@log('zhixing')
def ZiRanShu(m):
    n = 1
    while n < m:
        yield n
        n = n + 1

sys11 = sys.path
print(sys11)

ziranshu = ZiRanShu(20000)
HuiShu = list(filter(IsHuiShu, ziranshu))
print("回数集合：",HuiShu)


jieshou = str2int('13205')
print('ahahahahahhaahhahahhaha:::::',jieshou)


L =list(map(TheFirstWordCapitalize,['adam', 'LISA', 'barT']))
print('转换后的字符串：',L,'\n转换完毕')

prod = reduce(do_reduce_prod,[1,2,3,6,6,3])
print('相乘后的数值：',prod,'\n计算完毕')

yanghui = []
for yanghui in YangHuiSanJiao(13):
    print(yanghui)

print('杨辉三角完成')



maxnum = 9
L1 = []
for maxnum1 in Fibonacci(maxnum):
    print(maxnum1)

#print(L1)
print('Fibonacci数列完成')


numbers = [1,2,3,4,5,6]
print("youbujide")
print(numbers)
sum1 = calc(*numbers)
print(sum1)

a = eval(input('a:'))
b = eval(input('b:'))
c = eval(input('c:'))
kw = ['111',555]
s1 = jiefangcheng(a,b,c,*kw)
print(s1)
#print('%fx2 + %fx + c = 0'%jiefangcheng(a,b,c))

score_thisyear = eval(input('今年的成绩'))
score_lsatyear = eval(input('去年的成绩'))
Multiple_ReturnValue(score_thisyear,score_lsatyear)
