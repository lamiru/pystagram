from django.conf.urls import url

urlpatterns = [
    url(r'^profile/$', 'accounts.views.profile_detail'),
]
