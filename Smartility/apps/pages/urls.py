from django.conf.urls import patterns, include, url

urlpatterns = patterns('Smartility.apps.pages.views',
    url(r'^$', 'index'),
)
