from django.shortcuts import render
from django.http import JsonResponse
from .selenium.web_scraping import get_environmental_evaluation


# Create your views here.

def get_environmental_info(request):
    response = get_environmental_evaluation()
    return  JsonResponse({'response': str(response)}, status=200, safe=False)
