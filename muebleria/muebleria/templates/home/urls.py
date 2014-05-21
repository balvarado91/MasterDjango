from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('home.views',

   url(r'^$','vista_principal',name='la_vista_principal'),

)
