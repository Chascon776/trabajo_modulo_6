from django.contrib import admin
from .models import vehiculos
# Register your models here.
class vehiculoAdm(admin.ModelAdmin):
        list_display = ("marca", "modelo",)


admin.site.register(vehiculos, vehiculoAdm)

