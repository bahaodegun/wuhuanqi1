# /usr/bin/env python
# -*- coding: UTF-8 -*-
class demo():
    a=1
    _b=2
    __c=3
    def abc(self):
        print self.a
    def bcd(self):
        print self._b
    def cde(self):
        print self.__c
# print demo().a
# print demo().abc()
# print demo()._b
# print demo().bcd()
print(demo().cde())

