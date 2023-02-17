from django.urls import path
from . import views

urlpatterns = [
    path('get_citybike_network_info/', views.get_citybike_network_info, name='get_citybike_network_info'),
]