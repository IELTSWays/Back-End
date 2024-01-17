from django.contrib import admin
from exam.models import Test
from django.db import models

class TestAdmin(admin.ModelAdmin):
    list_display = ('test_id','name','skill', 'type', 'book')
admin.site.register(Test, TestAdmin)