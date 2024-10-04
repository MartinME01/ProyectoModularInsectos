from django.contrib import admin
from .models import Insectos, Estado

# Register your models here.

class InsectosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Insectos, InsectosAdmin)
admin.site.register(Estado)
