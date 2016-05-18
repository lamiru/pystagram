from django.conf.urls import url

urlpatterns = [
    url(r'^signup/$', 'accounts.views.signup'),
    url(r'^profile/$', 'accounts.views.profile_detail'),
]
