from django.views import View
from django.shortcuts import render

class GithubDetail(View):

    def get(self, request, *args, **kwargs):
        github_data = request.session.pop("github_data")
        return render(self.request,
                      'github_detail/index.html',
                      {'github_data': github_data}
                      )