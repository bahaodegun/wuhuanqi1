# /usr/bin/env python
# -*- coding: UTF-8 -*-
import requests

url="https://www.baidu.com/s?ie=utf-8&csq=1&pstg=20&mod=2&isbd=1&cqid=c0e7e9940002c0cd&istc=743&ver=RdcaGtY_Qe4aje7d5KKDmO9W10ZzWyyOCYC&chk=5c273e40&isid=A086763CAC226609&ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%90%B4%E6%A1%93%E7%A5%BA&rsv_pq=bbf5020e0002fd52&rsv_t=4134gk6Pr5UMFvnrjndVjKSB8IOjJUyovK5%2FiBRCtB6JhBRuffFrRLg%2Fq3A&rqlang=cn&rsv_enter=1&rsv_sug3=30&rsv_sug1=38&rsv_sug7=101&rsv_sug2=0&inputT=12500&rsv_sug4=27033&f4s=1&_ck=80109.0.-1.-1.-1.-1.-1&rsv_isid=26523_1441_21108_28205_28131_27750_28140&isnop=1&rsv_stat=-2&rsv_bp=1"
data={"wd":"吴桓祺"
}
res = requests.post(url,data)
print res.text