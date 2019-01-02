# /usr/bin/env python
# -*- coding: UTF-8 -*-
import copy
a=[1,2,3,["a","b"]]
#2、copy浅拷贝，没有拷贝子对象，所以原始数据改变，子对象会改变
b = copy.copy(a)
print(b)
#结果：[1, 2, 3, ['a', 'b']]
a.append(5)
print(a)
#结果：[1, 2, 3, ['a', 'b'], 5]
print(b)
#结果：[1, 2, 3, ['a', 'b']]   #b列表对象的值没有变。
a[3].append('cccc')  #给alist的子列表对象增加了值
print(b)
#结果：[1, 2, 3, ['a', 'b',"cccc"]]  #b中的子列表对象也同步发生了修改。
print(a)
#结果：[1, 2, 3, ['a', 'b',"cccc"], 5]


