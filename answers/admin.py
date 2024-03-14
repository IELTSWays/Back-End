from django.contrib import admin
from answers.models import TestCorrectAnswer, TestFullCorrectAnswer, Answer, TestMediaAnswer, MediaAnswer
from django.db import models
from ckeditor.widgets import CKEditorWidget
from django import forms



class TestCorrectAnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'book')
    list_filter = ('skill', 'book', 'skill')
    search_fields = ['name',]
admin.site.register(TestCorrectAnswer, TestCorrectAnswerAdmin)



class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class TestFullCorrectAnswerAdmin(admin.ModelAdmin):
    from ckeditor.widgets import CKEditorWidget
    list_display = ('name','skill', 'type', 'book')
    inlines = [AnswerInline, ]
admin.site.register(TestFullCorrectAnswer, TestFullCorrectAnswerAdmin)





class MediaAnswerInline(admin.TabularInline):
    model = MediaAnswer
    extra = 1

class TestMediaAnswerAdmin(admin.ModelAdmin):
    list_display = ('name','skill', 'type', 'book')
    inlines = [MediaAnswerInline, ]
admin.site.register(TestMediaAnswer, TestMediaAnswerAdmin)

