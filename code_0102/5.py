# /usr/bin/env python
# -*- coding: UTF-8 -*-
# 编写一个程序实现阶乘：1×2×3×4...×n
def sum(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    return s
print sum(4)