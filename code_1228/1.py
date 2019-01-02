# /usr/bin/env python
# -*- coding: UTF-8 -*-
# 编写一个名为FormatUrl的函数，对输入的urlstr进行检查和必要的格式化处理，
# 编程语言不限（lua、python、java均可）（8分）
# 要求:
# a) 剔除空格、回车符
# b) 将“&amp;”替换为“&”
# c) 检查字符串头，如果没有类似
# “http://”、“https://”、“ftp://”这样的URL头的话，就默认添加“http://”为URL头
import string
# a= " fdafa f&amp;dafa /n \nfdaff  fdas &amp;"
key = r"http://www.nsfbuhwe.com  https://www.auhfisna.com \n ftp://www.fdsafad.com"
def FormatUrl(str):
    a1=["https://","ftp://"]
    for item in a1:
        # print(item)
        if str.find(item)!=-1 ==True:
            print str.replace("https://","http://").str.replace(" ","").replace("\n","").replace("&amp;","&")
    print str.replace("https://","http://").str.replace(" ","").replace("\n","").replace("&amp;","&")
    #     str.find(a1)!=-1 :
    #     str.replace('https://','http://').str.replace(" ","").replace("\n",'').replace('&amp;','&')
    # elif str.find(b1)!=-1:
    #     str.replace('ftp://','http://').str.replace(" ","").replace("\n",'').replace('&amp;','&')
    # return str
print FormatUrl(key)
# p1 = r"https*://"
# pattern1 = re.compile(p1)
# print pattern1.findall(key)