#coding=utf-8
import urllib2
import urllib
import time
from bs4 import BeautifulSoup
from userinfo import HEADERS, INFO
import json


def doValidator(size, url):
    profile = urllib2.Request("http://www.nikestore.com.cn/transaction/doValidatorQsGoToTransactionCheck2",
                              data=urllib.urlencode({"upc": size, "count": "1"})
    )
    for key in HEADERS:
        profile.add_header(key, HEADERS[key])
    profile.add_header("Referer", "%s###" % url)
    profile.add_header("Content-Length", "%s" % len(str(urllib.urlencode({"upc": size, "count": "1"}))))
    profileresp = urllib2.urlopen(profile)
    try:
        json_obj = json.loads(profileresp.read())
        print json_obj
        if json_obj.get("commonTransactionBackWarnEntity")["isSuccess"]:
            return True
        else:
            print json_obj.get("commonTransactionBackWarnEntity")["description"]
            return False
    except Exception, e:
        print e

def qsReq():
    qs_req = urllib2.Request("http://www.nikestore.com.cn/transaction/create/qs?loxiaflag=%d" % int(time.time() * 1000),
                             data=urllib.urlencode(INFO))
    for key in HEADERS:
        qs_req.add_header(key, HEADERS[key])
    qs_req.add_header("Referer", "http://www.nikestore.com.cn/transaction/check/qs")
    qs_req.add_header("Content-Length", "%s" % len(str(urllib.urlencode(INFO))))
    qs_resp = urllib2.urlopen(qs_req)
    json_obj = json.loads(qs_resp.read())
    isSuccess = json_obj.get("transactionCreateBackWarnEntity")["isSuccess"]
    msg = json_obj.get("transactionCreateBackWarnEntity")["description"]
    print json_obj
    print msg
    return isSuccess, msg

def getSizeSet(url):
    result = dict()
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
    for i in soup.find_all("ul", attrs={"class": "select-box-size"}):
        for x in i.children:
            if x.string.strip() in ["42","42.5","43","44","41"]:
                result[x.string.strip()] = x.get("currupc")
    return result