__author__ = 'xiaojing'
from django.conf.urls import patterns, include, url


urlpatterns = patterns('nikestore.views',
                       url("^getimg/$", "getCode", name="getCode"),
                       url("^getsize/(?P<url>(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)/$",
                           "getSize", name="getSize"),
)