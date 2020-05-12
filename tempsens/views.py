from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class Index(View):
    path = "tempsens/index.html"

    def get(self, request):
        return render(request, self.path)
