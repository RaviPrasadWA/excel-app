from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^progress-bar-upload/$', views.ProgressBarUploadView.as_view(), name='progress_bar_upload')
]
