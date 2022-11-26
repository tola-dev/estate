from django.contrib import admin
from .models import Location, Buy_property, Sale_property, Mortgage_property, Rent_property, Profile

# Register your models here.

admin.site.register(Location)
admin.site.register(Buy_property)
admin.site.register(Sale_property)
admin.site.register(Rent_property)
admin.site.register(Mortgage_property)
admin.site.register(Profile)
