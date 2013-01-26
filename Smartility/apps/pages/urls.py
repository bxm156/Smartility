from django.conf.urls import patterns, include, url

urlpatterns = patterns('Smartility.apps.pages.views',
    url(r'^$', 'index'),
    url(r'^channel.html$', 'facebook_channel'),
)
