from django.shortcuts import render
import requests
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Network, Location, Station, StationExtra
from .create_networks.create_networks import create_network
# Create your views here.

def index(request):
    pass

def get_network_info(request):
    # Get information from the API
    if request.method == 'GET':
        url = 'http://api.citybik.es/v2/networks/bikesantiago'
        r = requests.get(url).json()
        network = r['network']
        if Network.objects.filter(id=network['id']).exists() == False:
            # If information is not in the database, create the citybike network in the db.
            network_location = network['location']
            network_stations = network['stations']
            create_network(network, network_location, network_stations)
        return JsonResponse(network, status=200)
