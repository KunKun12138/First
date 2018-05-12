#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'LIUYI'

import struct

class bmptest(object):
    def isbmp(self,road):
        with open(road, 'rb') as f:
            bmpfile = f.read(30)
            print(bmpfile, type(bmpfile))  # 19by
            j = struct.unpack('>ccIIIIIIHH', bmpfile)
            print(j, type(j),j[0])
            if(j[0] == b'B' and j[1] == b'M'):
                print("\n%s是.bmp格式文件" % road)
                print("位图大小为%s * %s"%(j[-4],j[-3]))
                print("颜色数为：%s"%j[-1])
            else:
                print("\n%s不是.bmp格式文件"%road)

if __name__ == '__main__':
    whichfile = bmptest()
    whichfile.isbmp("F://test.bmp")
    whichfile.isbmp("F://test.txt")