from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path("disable_led",views.DisableLed.as_view(), name="disable"),
]
