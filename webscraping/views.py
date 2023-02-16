from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def get_environmental_info(request):
    response = "hola"
    return  JsonResponse({'response': str(response)}, status=200)
