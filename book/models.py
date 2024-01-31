from django.db import models
from django.utils.html import format_html


class Book(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=256,null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    academic_cover_photo = models.ImageField(upload_to='books',default="books/default.png")
    general_cover_photo = models.ImageField(upload_to='books',default="books/default.png")
    academic = models.BooleanField(default=False)
    general = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    def academic_cover(self):
        return format_html("<img width=40 src='{}'>".format(self.academic_cover_photo.url))

    def general_cover(self):
        return format_html("<img width=40 src='{}'>".format(self.general_cover_photo.url))



class Product(models.Model):
    id = models.CharField(max_length=128,primary_key=True,unique=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    #skill_choices = (("listening", "listening"), ("reading", "reading"), ("writing", "writing"))
    #skill = models.CharField(choices=skill_choices, max_length=128)
    type_choices = (("academic", "academic"), ("general", "general"))
    type = models.CharField(choices=type_choices, max_length=128)
    #listening = models.BooleanField(default=True)
    #reading = models.BooleanField(default=True)
    #writing = models.BooleanField(default=True)
    enable = models.BooleanField(default=True)



