from django.conf.urls import patterns, include, url

urlpatterns = patterns('Smartility.apps.energydata.views',
    url(r'^$', 'index'),
    url(r'^(?P<user_id>[0-9]+)/$', 'get_data'),
)
