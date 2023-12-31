from django.db import models
from book.models import Book
from ckeditor.fields import RichTextField
from exam.utils import random_N_chars_str
from accounts.models import User


class Test(models.Model):
    test_id = models.CharField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=128,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_choices = (("listening","listening"),("reading","reading"),("writing","writing"))
    skill = models.CharField(choices=skill_choices,max_length=128)
    type_choices = (("academic","academic"),("general","general"))
    type = models.CharField(choices=type_choices, max_length=128)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    answers = models.JSONField(null=True, blank=True)
    test_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.test_id:
            self.test_id = random_N_chars_str(12)
        super(Test, self).save()

    def __str__(self):
        return str(self.skill) +'|'+ str(self.type) +'|'+ str(self.id)

