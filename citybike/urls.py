from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('get_info/', views.get_network_info, name='get_info')
]