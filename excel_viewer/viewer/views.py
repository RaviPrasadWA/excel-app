import os
import time
from .models import File_
import pyexcel as _excel_
from .forms import FileForm
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect, render_to_response



class ProgressBarUploadView(View):
    def get(self, request):
        files_list = File_.objects.all()
        return render(self.request,
                      'viewer/progress_bar_upload/index.html',
                      {'files': files_list}
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

class DetailView(View):

    def get(self, request, file_id):

        def wait_until_file_is_generated(file_path):
            time_to_wait = 10
            time_counter = 0
            while not os.path.exists(file_path):
                time.sleep(1)
                time_counter += 1
                if time_counter > time_to_wait:
                    break

        file_ = File_.objects.get(id=file_id)
        if file_:
            generated_file = "me{_id_}.sortable.html".format(_id_=str(file_id))
            sheet = _excel_.get_sheet(file_name=file_.file.path)
            sheet.save_as("generated/{path}".format(path=generated_file)
                          , display_length=10)
        wait_until_file_is_generated("generated/{path}".format(path=generated_file))
        return render_to_response(generated_file)
