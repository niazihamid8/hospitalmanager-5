from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SampleProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','myapp.views.home',name='home'),
    url(r'^default/$','myapp.views.default',name='default'),
    url(r'^login/$', 'myapp.views.login',name='login'),
    url(r'^users/$', 'myapp.views.users',name='login'),
    url(r'^news/$', 'myapp.views.news',name='news'),
    url(r'^list/$', 'myapp.views.List',name='list'),
    url(r'^rss/delete/(\w+)/$', 'myapp.views.rssdelete'),
    url(r'^register/$', 'myapp.views.reg'),
    url(r'^registersave/$', 'myapp.views.submit'),
    url(r'^admin/users/$', 'myapp.views.listusers'),
    url(r'^admin/users/delete/([^/]+)/$', 'myapp.views.deluser',name=''),
    url(r'^admin/users/edit/([^/]+)/$', 'myapp.views.edituser',name='edituser'),
)
