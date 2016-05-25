from django.conf.urls import url

urlpatterns = [
    url(r'^signup/$', 'accounts.views.signup'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'django.contrib.auth.views.login'}),
    url(r'^profile/$', 'accounts.views.profile_detail'),
    url(r'^profile/edit/$', 'accounts.views.profile_edit'),
    url(r'^(?P<username>\w+)/follow/$', 'accounts.views.user_follow', name='user_follow'),
    url(r'^(?P<username>\w+)/unfollow/$', 'accounts.views.user_unfollow', name='user_unfollow'),
]
