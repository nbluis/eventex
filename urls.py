from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'core.views.index'),
)

urlpatterns	+= staticfiles_urlpatterns()