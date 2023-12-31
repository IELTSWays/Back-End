from django.contrib import admin
from book.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('cover', 'name', 'academic', 'general')
admin.site.register(Book, BookAdmin)