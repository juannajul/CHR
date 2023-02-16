
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('citybike/', include('citybike.urls')),
    path('scraping/', include('webscraping.urls'))
]
