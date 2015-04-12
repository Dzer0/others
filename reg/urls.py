from django.conf.urls import patterns, include, url
from django.contrib import admin
from www.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'reg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg/$',reg),
    url(r'^lie/$',lie),
    url(r'^login/$',login),
    url(r'logout',logout),
    # url(r'^validate/$', 'validate', name='validate'),
    url(r'^up/$',up),
)
