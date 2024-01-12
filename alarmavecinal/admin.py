from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Neighbor, Neighborhood, Device, Event
from django.contrib.auth.models import User


# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "serial"]

class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ["name", "police", "fireemergency", "admin", "master", "device"]

class NeighborInline(admin.StackedInline):
    model = Neighbor
    can_delete = False
    verbose_name_plural = "neighbors"

class UserAdmin(BaseUserAdmin):
    inlines = [NeighborInline]

admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Event)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)



