# /usr/bin/env python
# -*- coding: UTF-8 -*-
import re
import requests

str="{code:200}"
non=str.replace("\n","")
result = re.match("^\{co.*?(\d+)",str)
print result
print result.group(1)