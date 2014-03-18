#coding=utf-8
from bs4 import BeautifulSoup
from bs4 import element
import urllib2
import time


def select_size(url):
    avail = []
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
    for i in soup.find_all("ul", attrs={"class": "select-box-size"}):
        for x in i.children:
            if x.string.strip() in ["42","42.5","43","44","41"]:
                print x.get("currupc")
            #     avail.append(x.get("currupc"))

    return avail


INFO = {
    "shippingInfoCommand.name": "晓晶",
    "shippingInfoCommand.province": "北京",
    "shippingInfoCommand.city": "北京市",
    "shippingInfoCommand.district": "东城区",
    "shippingInfoCommand.address": "北京市东城区青年湖西里湖景苑小区3号楼3门102",
    "shippingInfoCommand.zipcode": "100011",
    "shippingInfoCommand.mobile": "13717710995",
    "shippingInfoCommand.telephone": "",
    "shippingInfoCommand.email": "xsuperj@sina.com",
    "shippingInfoCommand.shippingMethod": "1",
    "shippingInfoCommand.deliveryTimePeriod": "WORK_DAY_ONLY",
    "shippingInfoCommand.memo": "",
    "paymentInfoCommand.paymentType": "6",
    "invoiceInfoCommand.invoiceTitle": "个人",
    "omnitureProducts": "638426-700",
    "paymentInfoCommand.bankcode": "",
    "date": "%s GMT+0800 (中国标准时间)" % time.strftime('%a %b %d %Y %H:%M:%S', time.localtime(time.time()))
}

HEADERS = {"Accept-Language": "zh-cn",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "Accept": "*/*",
               "Accept-Encoding": "deflate",
               "X-Requested-With": "XMLHttpRequest",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11",
               "Connection": "keep-alive",
               "Host": "www.nikestore.com.cn",
               "Pragma": "no-cache",
               "DNT": "1",
               "Referer": "http://www.nikestore.com.cn/member/login.htm",
    }

select_size("http://www.nikestore.com.cn/product/631733-106/detail.htm")