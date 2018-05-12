#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'LIUYI'

import pickle
import json
import os


###每打开一个IO流只能使用一次load方法或loads方法，否则报错“Out of Iuput”
###json序列化则没有限制，可以进行多次反序列化
def pickleTest(road):
    try:
        print("---不写入文件pickle")
        d = dict(a=1, b='pickle')
        ddumps = pickle.dumps(d)
        print("序列化后：",ddumps)
        print("反序列化后：",pickle.loads(ddumps))

        print("\n---写入文件pickle")
        #pickle序列化必须以二进制方式写入，json序列化则不需要
        with open('F://test.txt', 'wb') as f:
            pickle.dump(d, f)

        with open(road, 'rb') as f1:
            yuanwen = f1.read()
            print("dump写入的原文为:",yuanwen)
            d1 = pickle.loads(yuanwen)
            print("反序列化结果:", d1)

        with open(road, 'rb') as f1:
            size = f1.__sizeof__()
            print("文件大小：", size)
            if os.path.getsize(road) > 0:
                d2 = pickle.load(f1)
                print(d2)
    except EOFError:
        print("Out of Input")
        return None


def jsonTest(road):
    d = dict(a=1, b='json')

    print("---不写入文件Jsom")
    Jjsons = json.dumps(d)
    print("序列化后：", Jjsons)
    print("反序列化后：", json.loads(Jjsons))

    print("\n---写入文件Jsom")
    with open('F://test1.txt', 'w') as f:
        json.dump(d,f)

    with open(road, 'r') as f:
        yuanwen = f.read()
        print("dump写入的原文为:", yuanwen)
        d1 = json.loads(yuanwen)
        print("反序列化后:", d1)

        #yuanwen = f.read()
        #print("dump写入的原文为:", yuanwen)
        d2 = json.loads(yuanwen)
        print("反序列化后:", d2)


pickleTest('F://test.txt')
jsonTest('F://test1.txt')