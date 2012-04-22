from django.conf.urls.defaults import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'vdrinking.bmi.views.home', name='home'),
    url(r'^bmi/(?P<game_id>\d+)/$', 'vdrinking.bmi.views.detail'),
    # url(r'^vdrinking/', include('vdrinking.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), 
    url(r'^accounts/create/$', 'vdrinking.bmi.views.create'),
    # url(r'^accounts/profile/(?user-id)/$', 'vdrinking.bmi.views.profile'), 
)

urlpatterns += staticfiles_urlpatterns()
