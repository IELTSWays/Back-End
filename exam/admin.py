from django.contrib import admin
from exam.models import Test


class TestAdmin(admin.ModelAdmin):
    list_display = ('skill', 'type', 'Book')
admin.site.register(Test, TestAdmin)