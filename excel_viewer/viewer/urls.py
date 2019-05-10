from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^progress-bar-upload/$', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    url(r'^detail/(?P<file_id>\d+)/$', views.DetailView.as_view(), name='detail_view'),
]
