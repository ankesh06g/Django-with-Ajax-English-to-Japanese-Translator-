from django.urls import path

from . import views

app_name = "engtojap"

urlpatterns = [
    path('', views.home, name='index'),
    path('translator', views.translator, name='translator'),
]