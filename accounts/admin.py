from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'created_at', 'is_profile_fill')
admin.site.register(User, UserAdmin)

