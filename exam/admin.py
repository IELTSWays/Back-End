from django.contrib import admin
from exam.models import Test, TestPrice
from django.db import models

class TestAdmin(admin.ModelAdmin):
    list_display = ('test_id','name','skill', 'type', 'book')
admin.site.register(Test, TestAdmin)



class TestPriceAdmin(admin.ModelAdmin):
    list_display = ('listening','reading','writing', 'speaking')
admin.site.register(TestPrice, TestPriceAdmin)