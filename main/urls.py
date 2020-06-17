from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('health_check', views.health_check),
    path('', views.home),
]
