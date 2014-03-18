#coding=utf-8
import time

INFO = {
    "shippingInfoCommand.name": "杨利伟",
    "shippingInfoCommand.province": "北京",
    "shippingInfoCommand.city": "北京市",
    "shippingInfoCommand.district": "东城区",
    "shippingInfoCommand.address": "北京市东城区和平里北街",
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