from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<uuid>[0-9a-f]{32})/$', 'blog.views.detail'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.detail'),
    url(r'^new/$', 'blog.views.new'),
    url(r'^(?P<pk>\d+)/edit/$', 'blog.views.edit'),
    url(r'^(?P<pk>\d+)/comments/new$', 'blog.views.comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'blog.views.comment_edit'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', 'blog.views.comment_delete'),
]
