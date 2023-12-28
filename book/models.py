from django.db import models
from django.utils.html import format_html


class Book(models.Model):
    name = models.CharField(max_length=256,null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    cover_photo = models.ImageField(upload_to='books')
    academic = models.BooleanField(default=False)
    general = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    def cover(self):
        return format_html("<img width=40 src='{}'>".format(self.cover_photo.url))
