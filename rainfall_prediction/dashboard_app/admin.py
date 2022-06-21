from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('date', 'pressure', 'max_temp',  'temp',  'min_temp', 'dewpoint', 'humidity', 'cloud', 'sunshine', 'wind_direction', 'wind_speed', 'rain_fall')

admin.site.register(Data, DataAdmin)
