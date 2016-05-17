from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<uuid>[0-9a-f]{32})/$', 'blog.views.detail'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.detail'),
    url(r'^new/$', 'blog.views.new'),
    url(r'^(?P<pk>\d+)/edit/$', 'blog.views.edit'),
]
