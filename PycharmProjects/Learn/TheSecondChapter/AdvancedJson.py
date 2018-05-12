#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'LIUYI'

import pickle
import json
import os

class Student(object):
    #__slots__ = ('name','sex','score','__dict__')
    def __init__(self,name,sex,score):
        self.name = name
        self.sex = sex
        self.score = score


def dict2Student(self,dict1):
    return Student(dict1['name'],dict1['age'],dict1['score'])


s = Student("liuyi","female","90")
print(s)

a1 = json.dumps(s, default=lambda obj: obj.__dict__)
print(a1)
with open("F://test1.txt","w") as f:
    d1 = json.dump(s,f,default=lambda obj: obj.__dict__)

    print(d1)

'''
with open("F://test1.txt","r") as f:
    stu = f.read()
    json.loads(f,object_hook=dict2Student)
'''