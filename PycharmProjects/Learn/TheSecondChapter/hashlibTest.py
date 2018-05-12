#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
__author__ = 'LIUYI'

import hashlib
import pickle
import os

userdb = {}

class login(object):
    def Register(self):
        global userdb
        name = input("请输入用户名：")
        password = input("请输入密码：")

        with open("F://userInfo.txt", "rb") as userInfo:
            userdb = userInfo.read()
            print(userdb)
            if os.path.getsize("F://test.txt") > 0:
                userdb = pickle.loads(userdb)
                print(userdb)
            else:
                userdb = {}

        if name not in userdb:
            userdb[name] = login.get_md5(name,password)

            with open("F://userInfo.txt","wb") as userInfo:
                pickle.dump(userdb,userInfo)

            print("注册成功，请登录")
            login.login()
        else:
            print("用户存在，请直接登录")
            login.login()

    def login(self):
        name = input("请输入用户名：")
        password = input("请输入密码：")
        password_md5 = login.get_md5(name, password)

        with open("F://userInfo.txt", "rb") as userInfo:
            userdb = userInfo.read()
            print(userdb)
            if os.path.getsize("F://userInfo.txt") > 0:
                userdb = pickle.loads(userdb)
                print(userdb)
            else:
                userdb = {}

        if name in userdb:
            if userdb[name] == password_md5:
                print("登录成功！")
            else:
                print("登录失败！请检查用户名和密码")
        else:
            print("用户不存在，请注册")
            login.Register()

    def get_md5(self,name,password):
        md5 = hashlib.md5()
        salt_str = name + password + 'salt_liuyi'
        md5.update(salt_str.encode('utf-8'))
        pw = md5.hexdigest()
        print("加密后："+pw)
        return pw

if __name__ == '__main__':
    login = login()
    #login.login()
    login.Register()