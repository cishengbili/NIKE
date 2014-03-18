from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from niketools import settings

admin.autodiscover()

urlpatterns = patterns('',
    url("^$","nikestore.views.login",{"template_name": "nikestore/login.html"}, name="login"),
    url("^limited/$","nikestore.views.limited",{"template_name": "nikestore/limited.html"}, name="limited"),
    url("^select/$","nikestore.views.selectSize",{"template_name": "nikestore/selectsize.html"}, name="select"),
    url("^app/",include("nikestore.urls",namespace="nikestore")),
    # Examples:
    # url(r'^$', 'niketools.views.home', name='home'),
    # url(r'^niketools/', include('niketools.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
