from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^detail/$', views.GithubDetail.as_view(), name='user_github_detail'),
]
