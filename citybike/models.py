from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Network(models.Model):
    """Network model"""
    name = models.CharField(max_length=255)
    id = models.SlugField(max_length=255, blank=False, null=False, primary_key=True)
    gbfs_href = models.URLField(max_length=300)
    href = models.CharField(max_length=255)
    company = ArrayField(models.CharField(max_length=255), size=10)

    def __str__(self):
        return self.name
    

class Location(models.Model):
    """Network location model."""
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=12)
    latitude = models.DecimalField(default=0, max_digits=12, decimal_places=9)
    longitude = models.DecimalField(default=0, max_digits=12, decimal_places=9)
    network = models.OneToOneField(Network, on_delete=models.CASCADE, related_name='network_location')

    def __str__(self):
        return self.city
    

class Station(models.Model):
    """Network station model."""
    empty_slots = models.IntegerField(default=0)
    free_bikes = models.IntegerField(default=0)
    id = models.CharField(max_length=255, unique=True, blank=False, null=False, primary_key=True)
    latitude = models.DecimalField(default=0, max_digits=12, decimal_places=9)
    longitude = models.DecimalField(default=0, max_digits=12, decimal_places=9)
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    network = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='network_station')

    def __str__(self):
        return self.name


class StationExtra(models.Model):
    station = models.OneToOneField(Station, on_delete=models.CASCADE, related_name='station_extra')
    address = models.CharField(max_length=255)
    altitude = models.DecimalField(default=0, max_digits=5, decimal_places=3)
    ebikes = models.IntegerField(default=0)
    has_ebikes = models.BooleanField(default=False)
    last_updated = models.IntegerField(default=0)
    normal_bikes = models.IntegerField(default=0)
    payment = ArrayField(models.CharField(max_length=255))
    payment_terminal = models.BooleanField(default=False)
    post_code = models.CharField(max_length=255, null=True, blank=True)
    renting = models.IntegerField(default=0)
    returning = models.IntegerField(default=0)
    slots = models.IntegerField(default=0)
    uid = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self):
        return self.uid
    