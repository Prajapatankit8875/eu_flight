import re
from django.contrib import admin
from .models import airport
# Register your models here.
airport.objects.all()
admin.site.register(airport) 
