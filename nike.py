#coding=utf-8
import StringIO
import gzip
import pprint
import urllib
import urllib2
import cookielib
import time
from selectsize import select_size, INFO, HEADERS
import json

# url = "http://www.nikestore.com.cn/product/310805-106/detail.htm"
# size = select_size(url, [u"42",u"42.5",u"43",u"44",u"44.5",u"45"])[0]
# print size


def login():
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    # reqlogin = urllib2.Request("http://www.nikestore.com.cn/member/login.htm")
    # urllib2.urlopen(reqlogin)
    print cj
    req = urllib2.Request("http://www.nikestore.com.cn/servlet/securityImage?0.507514755474403767")
    for key in HEADERS:
        req.add_header(key, HEADERS[key])
    resp = urllib2.urlopen(req, timeout=10)
    print cj
    img = resp.read()
    with open("1.jpeg", "wb") as f:
        f.write(img)
    b = raw_input(">>>")
    data = {"loginName": "xsuperj2012",
            "password": "xj198898",
            "passwordAgain": b,
            "rememberLoginName": "checked"}
    data = urllib.urlencode(data)
    req = urllib2.Request("http://www.nikestore.com.cn/member/login.json?loxiaflag=1392346369990",
                          data=data)
    for key in HEADERS:
        req.add_header(key, HEADERS[key])
    resp = urllib2.urlopen(req)
    if json.loads(resp.read()).get("loginRedirectPath") == "/":
        print "登录成功"
        for i in cj:
            print (i.name + '=' + i.value + ';')
        return True
    else:
        print json.loads(resp.read())
        return False


def addShoppingCart():
    profile = urllib2.Request("http://www.nikestore.com.cn/shoppingcart/add",
                              data=urllib.urlencode({"upc": size, "count": "1"})
    )
    for key in HEADERS:
        profile.add_header(key, HEADERS[key])
    profile.add_header("Referer", "%s#" % url)
    profile.add_header("Content-Length", "%s" % len(str(urllib.urlencode({"upc": size, "count": "1"}))))
    profileresp = urllib2.urlopen(profile)
    try:
        json_obj = json.loads(profileresp.read())
        print json_obj
        # if json_obj.get("commonTransactionBackWarnEntity")["isSuccess"]:
        #     return True
        # else:
        #     print json_obj.get("commonTransactionBackWarnEntity")["description"]
        #     return False
    except Exception, e:
        print e

def check():
    profile = urllib2.Request("http://www.nikestore.com.cn/transaction/checkValidateCode.json",
                              data=urllib.urlencode({})
    )
    for key in HEADERS:
        profile.add_header(key, HEADERS[key])
    profile.add_header("Referer", "http://www.nikestore.com.cn/transaction/check")
    profile.add_header("Content-Length","0")
    profileresp = urllib2.urlopen(profile)
    try:
        json_obj = json.loads(profileresp.read())
        print json_obj
        # if json_obj.get("commonTransactionBackWarnEntity")["isSuccess"]:
        #     return True
        # else:
        #     print json_obj.get("commonTransactionBackWarnEntity")["description"]
        #     return False
    except Exception, e:
        print e
def doValidator():
    profile = urllib2.Request("http://www.nikestore.com.cn/transaction/doValidatorQsGoToTransactionCheck2",
                              data=urllib.urlencode({"upc": size, "count": "1"})
    )
    for key in HEADERS:
        profile.add_header(key, HEADERS[key])
    profile.add_header("Referer", "%s###" % url)
    profile.add_header("Content-Length", "%s" % len(str(urllib.urlencode({"upc": "00823229699172", "count": "1"}))))
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

def normalReq():
    qs_req = urllib2.Request("http://www.nikestore.com.cn/transaction/create?loxiaflag=%d" % int(time.time() * 1000),
                             data=urllib.urlencode(INFO))
    for key in HEADERS:
        qs_req.add_header(key, HEADERS[key])
    qs_req.add_header("Referer", "http://www.nikestore.com.cn/transaction/check")
    qs_req.add_header("Content-Length", "%s" % len(str(urllib.urlencode(INFO))))
    qs_resp = urllib2.urlopen(qs_req)
    json_obj = json.loads(qs_resp.read())
    isSuccess = json_obj.get("transactionCreateBackWarnEntity")["isSuccess"]
    msg = json_obj.get("transactionCreateBackWarnEntity")["description"]
    print json_obj
    print msg
    return isSuccess, msg

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

def limit():
    isValid = False
    while True:
        if isValid:
            issuccess, msg = qsReq()
            if not issuccess:
                print msg
                time.sleep(1)
            else:
                print "完成"
                break
        else:
            if doValidator():
                isValid = True
            else:
                time.sleep(1)

if __name__ == "__main__":
    size = "00091205064379"
    size = "00091205073135"
    login()
    url = raw_input("url:")
    size = raw_input("size:")
    limit()
    # login()
    # addShoppingCart()
    # check()
    # normalReq()
