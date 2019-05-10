from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^github/detail/$', views.GithubDetail.as_view(), name='github_detail'),
]
