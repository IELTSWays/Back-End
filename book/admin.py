from django.contrib import admin
from book.models import Book, Product


class BookAdmin(admin.ModelAdmin):
    list_display = ('id','cover', 'name', 'academic', 'general')
admin.site.register(Book, BookAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','book', 'type', 'skill', 'enable')
admin.site.register(Product, ProductAdmin)