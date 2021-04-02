from django.contrib import admin
from .models import Classifications, Impacts, Orbits

# Register your models here.
admin.site.register(Classifications)
admin.site.register(Impacts)
admin.site.register(Orbits)