from django.contrib import admin

# Register your models here.
from app.models import car, bookvehicle, contact

admin.site.register(car) # car is registered  
admin.site.register(bookvehicle)
admin.site.register(contact)