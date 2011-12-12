from django.conf.urls.defaults import patterns, include, url

from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('sbhx_sbitter.sbitter.views',
    # Examples:
    url(r'^$', 'index', name='index_view'),
    url(r'^signup/$', 'signup', name='signup'),
    # url(r'^login/$', 'login_view', name='login_view'),
    url(r'^logout/$', 'logout_view', name='logout_view'),
    url(r'^post_sbit/$', 'post_sbit', name='post_sbit'),
    url(r'^accounts/login/$', login, kwargs=dict(template_name='login.html'),
        name='sitelogin'),
    url(r'^accounts/profile/$', 'profile', name='profile'),

    # url(r'^sbhx_sbitter/', include('sbhx_sbitter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
