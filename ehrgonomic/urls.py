from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ehrgonomic.views.home', name='home'),
    # url(r'^ehrgonomic/', include('ehrgonomic.foo.urls')),
    url(r'^sample/', 'records.views.sample', name='sample'),
    url(r'^old_sample/', 'records.views.old_sample', name='old_sample'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
