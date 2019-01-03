# /usr/bin/env python
# -*- coding: UTF-8 -*-
def isosceles_triangle(side_1,side_2,side_3):
    if side_1+side_2>side_3 or side_1+side_3>side_2 or side_2+side_3>side_1:
        print "可以构成三角形"
        if side_1==side_2 or side_1==side_3 or side_2==side_3:
            print "等腰三角形"
        else:
            print "不是等腰三角形"
    else:
        print("不能构成三角形")
isosceles_triangle(1,5,5)