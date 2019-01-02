# /usr/bin/env python
# -*- coding: UTF-8 -*-
a=[1,5,6,10,2,3]
for i in range(len(a)-1):
    print i
    for j in range(len(a)-1-i):
        print j
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print a