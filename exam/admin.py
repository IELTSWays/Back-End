from django.contrib import admin
from exam.models import Test
from ckeditor.widgets import CKEditorWidget
from django.db import models

class TestAdmin(admin.ModelAdmin):
    list_display = ('skill', 'type', 'book')
    formfield_overrides = { models.TextField: {'widget': CKEditorWidget},}
admin.site.register(Test, TestAdmin)