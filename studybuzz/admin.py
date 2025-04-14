from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Import your custom user model

admin.site.register(User, UserAdmin)  # Register User model in admin panel

from .models import Room,Topic,Message

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
admin.site.register(Room, RoomAdmin)
admin.site.register(Topic)
admin.site.register(Message)
