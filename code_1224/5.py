# /usr/bin/env python
# -*- coding: UTF-8 -*-
#二、请写出下列代码的运行结果
def f(str1,*args,**kwargs):
    print(str1,args,kwargs)

l = [1,2,3]
t = [4,5,6]
d = {"a":7,"b":8,"c":9}
f(1,2)#(1, (2,), {})
f(1,2,3,"python")#(1, (2, 3, 'python'), {})
f("python",a=1,b=2,c=3)#('python', (), {'a': 1, 'c': 3, 'b': 2})
f("python",l,d)#('python', ([1, 2, 3], {'a': 7, 'c': 9, 'b': 8}), {})
f("python",*t)#('python', (4, 5, 6), {})
f('python',*l,**d)#('python', (1, 2, 3), {'a': 7, 'c': 9, 'b': 8})
f("python",q="winning",**d)#('python', (), {'a': 7, 'q': 'winning', 'c': 9, 'b': 8})