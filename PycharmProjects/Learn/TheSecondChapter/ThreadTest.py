#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'LIUYI'

from multiprocessing import Process
from multiprocessing import Process, Queue
import os, time, random
import os
import subprocess

# 子进程要执行的代码
def run_proc(name,q):
    for i in range(5):
        print("第%d个"%i)
        print('Run child process %s (%s)...' % name,(os.getpid()))
        q.put(i)
'''
def run_proc(name,q):
    while True:
        print('Run child process %s (%s)...' % name,(os.getpid()))
        print('读取数据....')
        value = q.get(True)
        print('Get %s from queue.' % value)
'''
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    q = Queue()
    p = Process(target=run_proc, args=("haha",q,))
    #pr = Process(target=read, args=(q,))
    p = Process(target=run_proc, args=('名字',q,))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

    print("$ nslookup")
    p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\n10.123.65.56\nexit\n')
    print(output.decode('gbk'))
    print('Exit code:', p.returncode)