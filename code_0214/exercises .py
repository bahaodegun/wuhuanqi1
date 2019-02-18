# /usr/bin/env python
# -*- coding: UTF-8 -*-
list=[1,2,3,4,5]
def fu(x):
    return x**2
res=map(fu,list)
print res
# res=[i for i in res if i>10]
list1=[]
for i in res:
    if i > 10:
        list1.append(i)
print list1