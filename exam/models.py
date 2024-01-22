from django.db import models
from book.models import Book
from exam.utils import random_N_chars_str
from accounts.models import User



class TestPrice(models.Model):
    listening = models.IntegerField(default=0)
    reading = models.IntegerField(default=0)
    writing = models.IntegerField(default=0)
    speaking = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.listening) + ' | ' + str(self.reading) + ' | ' + str(self.writing) + ' | ' + str(self.speaking)




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

