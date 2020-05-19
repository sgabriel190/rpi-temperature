from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from .tasks import *

class Index(View):
    path = "tempsens/index.html"
    def get(self, request):
        task_result = getInfo.delay()
        info = task_result.get()
        return render(request, self.path, { 
            'temperature': info["temp"],
            'humidity': info["hum"],
            'local_time': info["time"],
         })


def disable_led(request):
    powerOffLed.delay()
    return redirect("/tempsens/")
