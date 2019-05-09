import time
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import FileForm
from .models import File_


class ProgressBarUploadView(View):
    def get(self, request):
        files_list = File_.objects.all()
        return render(self.request,
                      'viewer/progress_bar_upload/index.html',
                      {'photos': files_list}
                      )

    def post(self, request):
        time.sleep(
            1)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        form = FileForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            file_ = form.save()
            data = {'is_valid': True, 'name': file_.file.name, 'url': file_.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
