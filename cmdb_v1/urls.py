from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cmdb_v1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index.html/$', 'assets.views.index'),
    url(r'^index/$', 'assets.views.index'),
    url(r'^assets/', include('assets.urls')),
)
