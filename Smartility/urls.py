from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Smartility.views.home', name='home'),
    # url(r'^Smartility/', include('Smartility.foo.urls')),


    (r'', include('Smartility.apps.pages.urls')),
    (r'^data/', include('Smartility.apps.energydata.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #Begin django-allauth
    (r'^accounts/', include('allauth.urls')),
    #End django-allauth
)
