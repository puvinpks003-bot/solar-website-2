# CORRECT CODE
from django.apps import AppConfig

class SolarWebConfig(AppConfig):  # Renamed for clarity, but the 'name' field below is what matters most
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'solar_web'  # <-- Fix this line