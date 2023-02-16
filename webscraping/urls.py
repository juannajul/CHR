from django.urls import path
from . import views

urlpatterns = [
    path('get_environmental_info/', views.get_environmental_info, name='get_environmental_info')
]