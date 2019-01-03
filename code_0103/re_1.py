# /usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import re
html=requests.get("https://book.douban.com/").text
# pattern=re.compile("<li.*?cover.*?href='(.*?)'.*?title='(.*?)'.*?</div>",re.S)
result=re.findall('<a.*?title="(.*?)".*?</a>',html,re.S)
print result