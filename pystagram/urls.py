from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photos/$', 'photos.views.index'),
    url(r'^photos/(?P<pk>\d+)/$', 'photos.views.detail'),
]
