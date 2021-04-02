from django.contrib import admin
from .models import Classification, Impacts, Orbits

# Register your models here.
admin.site.register(Classification)
admin.site.register(Impacts)
admin.site.register(Orbits)