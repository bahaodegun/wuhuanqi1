# /usr/bin/env python
# -*- coding: UTF-8 -*-
#请写下列代码的运行结果
import copy
a = [1,2,3,4,["a","b"]]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append("c")

#请填根据以上规则填 写以下输出内容：
print('a = ',a)
print('b = ',b)
print('c = ',c)
print('d = ',d)