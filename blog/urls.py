from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<pk>\d+)$', 'blog.views.detail'),
]
