from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'photos.views.index'),
    url(r'^(?P<pk>\d+)', 'photos.views.detail'),
]
