from django.urls import path
from . import views  # <-- '.' means in the same directory

urlpatterns = [
    path('', views.index, name='index')
]
