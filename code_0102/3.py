# /usr/bin/env python
# -*- coding: UTF-8 -*-
# 七、根据要求实现对应的方法
# a) //等长的两个列表合并到一个字典
# keys = ["A","B","C"]
# values = ["1","2","3"]
# # 要求：合并成{"A":1,"B":2,"C":3},请用一行代码实现
# dict_1={}
# for i in range(len(keys)):
#     dict_1[keys[i]]=values[i]
# print dict_1
# # b)//合并两个列表并消除重复值
# list_1 = ["a","b","c","1","A","winning"]
# list_2 = ["a","python","string","1"]
# print set(list_1+list_2)
# c) //已知一个列表，根据字典中的x，由大到小排序这个列表
#  已知列表：
a = [{"x":1,"y":2},{"x":2,"y":3},{"x":3,"y":4}]
print len(a)
for i in range(len(a)-1):
    print(i)
    for j in range(len(a)-1-i):
        print(j)
        if a[j]["x"]>a[j+1]["x"]:
            a[j],a[j+1]=a[j+1],a[j]
print a