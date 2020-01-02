
from django.contrib import admin
from .models import Profile,Zones

admin.site.register(Profile)
admin.site.register(Zones)
admin.site.site_header="Administration"