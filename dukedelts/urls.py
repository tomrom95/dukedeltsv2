from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', 'dukedelts.views.home', name='home'),
   url(r'^alumniform', 'dukedelts.views.alumni', name='alumni'),
   url(r'^rushform', 'dukedelts.views.rush', name='rush'),
   url(r'^brothers', 'dukedelts.views.brothers', name='brothers'),
   url(r'^admin/view/', include(admin.site.urls)),
   url(r'^admin', 'dukedelts.views.adminlogin', name='adminlogin'),
   url('', include('social.apps.django_app.urls', namespace='social')),
   url('', include('django.contrib.auth.urls', namespace='auth')),
)

if settings.DEBUG is True:
	urlpatterns = patterns('',
   	url(r'^$', 'dukedelts.views.home', name='home'),
      url(r'^alumniform', 'dukedelts.views.alumni', name='alumni'),
      url(r'^rushform', 'dukedelts.views.rush', name='rush'),
   	url(r'^brothers', 'dukedelts.views.brothers', name='brothers'),
   	url(r'^admin/view/', include(admin.site.urls)),
      url(r'^admin', 'dukedelts.views.adminlogin', name='adminlogin'),
   	url('', include('social.apps.django_app.urls', namespace='social')),
   	url('', include('django.contrib.auth.urls', namespace='auth')),
   	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
	)+staticfiles_urlpatterns()
