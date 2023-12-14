from django.db import models
from book.models import Book


class Test(models.Model):
    skill_choices = (("listening","listening"),("reading","reading"),("writing","writing"))
    skill = models.CharField(choices=skill_choices,max_length=128)
    type_choices = (("academic","academic"),("general","general"))
    type = models.CharField(choices=type_choices, max_length=128)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    questions = models.TextField()

    def __str__(self):
        return str(self.skill) +'|'+ str(self.type) +'|'+ str(self.id)


