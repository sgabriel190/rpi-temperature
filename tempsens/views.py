from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .raspi.temp_sens import getInfo

class Index(View):
    path = "tempsens/index.html"

    def get(self, request):
        info = getInfo()
        return render(request, self.path, { 
            'temperature': info["temp"],
            'humidity': info["hum"],
            'time': info["time"],
         })
