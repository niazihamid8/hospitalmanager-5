from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SampleProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','myapp.views.home',name='home'),
    url(r'^login/$', 'myapp.views.login',name='login'),
)
