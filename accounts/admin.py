from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'user_type', 'created_at')
    #search_fields = ['name', 'province']
admin.site.register(User, UserAdmin)

