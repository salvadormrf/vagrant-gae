from django.conf.urls import patterns, include, url

from hello.views import HomeView
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    #url(r'^admin/', include(admin.site.urls)),
)
