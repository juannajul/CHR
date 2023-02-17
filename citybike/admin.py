from django.contrib import admin
from .models import *
# Register your models here.

class LocationInline(admin.StackedInline):
    model = Location
    can_delete = True

admin.site.register(Location)

class StationExtraInline(admin.StackedInline):
    model = StationExtra
    can_delete = True

admin.site.register(StationExtra)

class CustomStationAdmin(admin.ModelAdmin):
    inlines = (StationExtraInline, )

class StationInline(admin.StackedInline):
    model = Station
    can_delete = True

admin.site.register(Station, CustomStationAdmin)


class CustomNetworkAdmin(admin.ModelAdmin):
    inlines = (LocationInline, StationInline)

admin.site.register(Network, CustomNetworkAdmin)
