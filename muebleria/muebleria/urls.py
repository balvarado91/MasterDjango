import settings

from django.conf.urls import patterns, include, url

from django.http import HttpResponse

from django.contrib import admin


admin.autodiscover()


def hello(request):
	return HttpResponse("Hello world")
urlpatterns = patterns('',

   #url (r'^',include('home.urls')),

   url(r'^admin/', include(admin.site.urls)),

   url(r'^$', hello),

)
