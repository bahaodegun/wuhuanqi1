# /usr/bin/env python
# -*- coding: UTF-8 -*-
passwd={"admin":"123321","user1":"123456"}
# 1、设计一个登陆程序，不同的用户名和对应密码存在一个字典里面，输入正确的用户和密码去登陆，
# 2、首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名
# 3、当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应，则提示密码错误请重新输入。
# 4、如果密码输入错误超过三次，中断程序运行。
# 5、当输入密码错误时，提示还有几次机会
# 6、用户名和密码都输入成功的时候，提示登陆成功！
print type(passwd["admin"])
while True:
    user=str(input("请输入账号："))
    print type(user)
    if user == passwd["admin"]:
        break
    else:
        print "账号输入错误或不存在"
        continue
a=0
while True:
    pwd=str(input("请输入密码："))
    if a<3 and pwd == passwd["user1"]:
        print "登录成功！"
        break
    elif a<3:
        a+=1
        print a
        print "账号输入错误或不存在,还有{0}次机会".format(4-a)
    else:
        print "密码错误太多，结束"
        break