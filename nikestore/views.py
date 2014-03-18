#coding=utf-8
import cookielib
import json
from nikestore.util.limited import doValidator, qsReq, getSizeSet
import urllib
import urllib2
from django.http import HttpResponse
from django.shortcuts import render, redirect
from nikestore.util.userinfo import HEADERS
from nikestore.util.ajax import ajax_success

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)


def getCode(request):
    req = urllib2.Request("http://www.nikestore.com.cn/servlet/securityImage?0.507514755474403767")
    for key in HEADERS:
        req.add_header(key, HEADERS[key])
    img_resp = urllib2.urlopen(req, timeout=10)
    resp = HttpResponse()
    resp.write(img_resp.read())
    resp["Content-Type"] = "image/JPEG"
    resp["Cache-control"] = "no-cache"
    return resp

def getSize(request,url):
    size_set = getSizeSet(url)
    return ajax_success(size_set)


def login(request, template_name):
    if request.method == "POST":
        code = request.POST.get("code")
        data = {"loginName": "xsuperj2012",
                "password": "xj198898",
                "passwordAgain": code,
                "rememberLoginName": "checked"}
        data = urllib.urlencode(data)
        req = urllib2.Request("http://www.nikestore.com.cn/member/login.json?loxiaflag=1392346369990",
                              data=data)
        for key in HEADERS:
            req.add_header(key, HEADERS[key])
        resp = urllib2.urlopen(req)
        result = resp.read()
        print result
        if json.loads(result).get("loginRedirectPath") == "/":
            for i in cj:
                print (i.name + '=' + i.value + ';')
            return redirect("limited")
        else:
            print json.loads(result)
    return render(request, template_name, dict(path=request.META.get("PATH_INFO")))


def limited(request, template_name):
    if request.method == "POST":
        url = request.POST.get("url")
        size = request.POST.get("size")
        doValidator(size, url)
        qsReq()
    return render(request, template_name, dict(path=request.META.get("PATH_INFO")))

def selectSize(request, template_name):
    return render(request,template_name)
