from django.contrib import admin
from answers.models import TestCorrectAnswer
from ckeditor.widgets import CKEditorWidget
from django.db import models


class TestCorrectAnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'book')
admin.site.register(TestCorrectAnswer, TestCorrectAnswerAdmin)