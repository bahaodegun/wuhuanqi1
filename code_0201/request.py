# /usr/bin/env python
# -*- coding: UTF-8 -*-
import urllib2
import urllib
import cookielib
import json
import httplib
import re
import requests
headers={"content-type":"application/json",'user-sessionid': '92ba3541bc7c804d90b50403f3c4d6d0'}
url="http://10.148.67.131:38080/cloudapi/DefectService/defect/queryAllDefect"
data={"keyword": "1", "pageSize": "10", "pageNo": "1", "function_requirement_id": "1"}
# res=requests.post(url,data,headers)
# print res.json()
req = requests.post(url ,
                headers=headers ,
                data = json.dumps(data))
print req.json()['code']