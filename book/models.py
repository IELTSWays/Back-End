from django.db import models
from django.utils.html import format_html


class Book(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=256,null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    cover_photo = models.ImageField(upload_to='books')
    academic = models.BooleanField(default=False)
    general = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    def cover(self):
        return format_html("<img width=40 src='{}'>".format(self.cover_photo.url))



class Product(models.Model):
    id = models.CharField(max_length=128,primary_key=True,unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    skill_choices = (("listening", "listening"), ("reading", "reading"), ("writing", "writing"))
    skill = models.CharField(choices=skill_choices, max_length=128)
    type_choices = (("academic", "academic"), ("general", "general"))
    type = models.CharField(choices=type_choices, max_length=128)
    enable = models.BooleanField(default=True)



