from ..models import Network, Location, Station, StationExtra
from django.db import IntegrityError
from django.http import JsonResponse

def create_network(network, network_location, network_stations):
    # Create network with the api information.
    try:
        # Create network.
        create_network = Network.objects.create(
            name=network['name'], id=network['id'],
            gbfs_href=network['gbfs_href'], href=network['href'],
            company=network['company']
        )
        create_network.save()
        # Create network location.
        create_network_location(network_location, create_network)
        # Create network stations.
        create_network_station(network_stations, create_network)
    except IntegrityError as e:
        return JsonResponse({"error": str(e)}, status=404)


def create_network_location(network_location, network):
    # Create network location for citybike network.
    create_network_location = Location.objects.create(
                city=network_location['city'], country=network_location['country'],
                latitude=network_location['latitude'], longitude=network_location['longitude'],
                network=network
        )
    create_network_location.save()
    return create_network_location

def create_network_station(network_stations, network):
    # Create network stations for citybike network.
    for station in network_stations:
            create_network_station = Station.objects.create(
                    empty_slots=station['empty_slots'], free_bikes=station['free_bikes'],
                    id=station['id'], latitude=station['latitude'], longitude=station['longitude'],
                    name=station['name'], timestamp=station['timestamp'], network=network
            )
            create_network_station.save()
            # Create stations extra data.
            station_extra_data = station['extra']
            create_station_extra = StationExtra.objects.create(
                    station=create_network_station, address=station_extra_data['address'],
                    altitude=station_extra_data['altitude'], ebikes=station_extra_data['ebikes'],
                    has_ebikes=station_extra_data['has_ebikes'], last_updated=station_extra_data['last_updated'],
                    normal_bikes=station_extra_data['normal_bikes'], payment=station_extra_data['payment'],
                    payment_terminal=station_extra_data['payment-terminal'],
                    renting=station_extra_data['renting'], returning=station_extra_data['returning'],
                    slots=station_extra_data['slots'], uid=station_extra_data['uid']
            )
            post_code = station_extra_data.get('post_code')
            if post_code != None:
                create_station_extra.post_code = post_code
                create_station_extra.save()
    return Station.objects.filter(network=network)    
    