from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from alarmavecinal.models import *
from django.contrib.auth.models import User


# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "serial"]

class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ["name", "police", "fireemergency", "master", "device"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(admin=request.user)

class NeighborInline(admin.StackedInline):
    model = Neighbor
    can_delete = False
    verbose_name_plural = "neighbors"

class UserAdmin(BaseUserAdmin):
    inlines = [NeighborInline]
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
            },
        ),
    )

    class Media:
        js = ["admin.js"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(neighbor__neighborhood__admin=request.user)

class EventsAdmin(admin.ModelAdmin):
    list_display = ["id", "message", "user", "timestamp", "delivered"]
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user__neighbor__neighborhood__admin=request.user)

class NeighborInline(admin.StackedInline):
    model = Neighbor
    can_delete = False
    verbose_name_plural = "neighbors"

admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Event, EventsAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)



