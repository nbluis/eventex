from django.contrib	import admin
from django.conf.urls.defaults import patterns, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'core.views.index'),
    (r'^admin/', include(admin.site.urls)),
    (r'^inscricao/', include('subscription.urls', namespace='subscription')),
)

urlpatterns	+= staticfiles_urlpatterns()
