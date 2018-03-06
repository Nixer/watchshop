from django.contrib import admin
from watchshopapp.models import WatchShop, Watch, Client


# Register your models here.
admin.site.register(WatchShop)
admin.site.register(Watch)
admin.site.register(Client)
