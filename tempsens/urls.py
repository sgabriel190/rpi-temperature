from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('disable_led/', views.disable_led, name="disable_led"),
    path('get_data_json/', views.get_data_json, name="get_data_json"),
]
