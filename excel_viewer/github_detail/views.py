from django.views import View
from django.shortcuts import render

class GithubDetail(View):

    def post(self, request, *args, **kwargs):
        print(dir(request))
        return 1