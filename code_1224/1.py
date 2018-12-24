# /usr/bin/env python
# -*- coding: UTF-8 -*-
# 需求：给定一个只包含正整数且非空的数组，返回该数组中重复次数最多的前N个数字
# （返回结果按重复次数从多到少降序排列，N不存在取值非法的情况），请用熟悉的语言实现该需求
# 。。。。。10分钟内写出来

a=[1,6,7,4,4,5,4,5,4,5,5,6,7,8,5,6,7,3,4,2,2,1,4,8,9,4,5,6]
dict_1={}
list_1=[]
for i in set(a):
#使用set去重
    dict_1[i] = a.count(i)
    #按写入字典，count计数
# print dict_1

res = sorted(dict_1.values(),reverse=True)
#sorted 按倒序排序  reverse=True 是按降序排序  默认false正序排序
# 字典的值取出来后按倒序排序  [7, 6, 4, 3, 2, 2, 2, 1, 1]
for num in res:
    for key,value in dict_1.items():
        print key,value
        #如果值在列表中不存在，则添加到结果列表中。
        if num == value and key not in list_1:

            list_1.append(key)
            print list_1
