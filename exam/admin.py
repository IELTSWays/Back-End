from django.contrib import admin
from exam.models import Test, TestPrice, SpeakingTest, WritingTest, TestHistory
from django.db import models

class TestAdmin(admin.ModelAdmin):
    list_display = ('test_id','name','skill', 'type', 'book','confirm' ,'is_expired')
    search_fields = ["test_id","name"]
admin.site.register(Test, TestAdmin)



class TestPriceAdmin(admin.ModelAdmin):
    list_display = ('listening','reading')
admin.site.register(TestPrice, TestPriceAdmin)



class SpeakingTestAdmin(admin.ModelAdmin):
    list_display = ('teacher','time', 'user')
admin.site.register(SpeakingTest, SpeakingTestAdmin)



class WritingTestAdmin(admin.ModelAdmin):
    list_display = ('marker', 'user')
admin.site.register(WritingTest, WritingTestAdmin)


class TestHistoryAdmin(admin.ModelAdmin):
    list_display = ('test','user','band_score', 'raw_score')
admin.site.register(TestHistory, TestHistoryAdmin)
