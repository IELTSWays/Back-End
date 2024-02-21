from django.contrib import admin
from answers.models import TestCorrectAnswer, TestFullCorrectAnswer, Answer
from django.db import models


class TestCorrectAnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'book')
    list_filter = ('skill', 'book', 'skill')
    search_fields = ['name',]
admin.site.register(TestCorrectAnswer, TestCorrectAnswerAdmin)







class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class TestFullCorrectAnswerAdmin(admin.ModelAdmin):
    list_display = ('name','skill', 'type', 'book')
    inlines = [AnswerInline, ]
admin.site.register(TestFullCorrectAnswer, TestFullCorrectAnswerAdmin)

