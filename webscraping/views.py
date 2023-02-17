from django.shortcuts import render
from django.http import JsonResponse
from .selenium.web_scraping import get_environmental_evaluation_projects, write_json


# Create your views here.

def get_environmental_info(request):
    """Get projects data from the url: https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"""
    response = get_environmental_evaluation_projects()
    # Create json file for the data.
    write_json(response)
    return  JsonResponse({'response': str(response)}, status=200, safe=False)
