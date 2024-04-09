from django.contrib import admin
from .models import Red

class RedAdmin(admin.ModelAdmin):
    pass

admin.site.register(Red, RedAdmin) 