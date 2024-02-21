from django.db import models
from exam.models import Test
from accounts.models import User
from book.models import Book



class TestCorrectAnswer(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    skill_choices = (("listening", "listening"), ("reading", "reading"), ("writing", "writing"))
    skill = models.CharField(choices=skill_choices, max_length=128)
    type_choices = (("academic", "academic"), ("general", "general"))
    type = models.CharField(choices=type_choices, max_length=128)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    answers = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.name) +'|'+ str(self.book)






class TestFullCorrectAnswer(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    skill_choices = (("listening", "listening"), ("reading", "reading"), ("writing", "writing"))
    skill = models.CharField(choices=skill_choices, max_length=128)
    type_choices = (("academic", "academic"), ("general", "general"))
    type = models.CharField(choices=type_choices, max_length=128)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) +'|'+ str(self.book)




class Answer(models.Model):
    test_answer = models.ForeignKey(TestFullCorrectAnswer,on_delete=models.CASCADE)
    question_number = models.IntegerField()
    answer = models.CharField(max_length=256, null=True, blank=True)
    question = models.CharField(max_length=256, null=True, blank=True)
    keywords = models.CharField(max_length=256, null=True, blank=True)
    full_answer = models.TextField(max_length=2500, null=True, blank=True)

    def __str__(self):
        return str(self.answer) + ' | ' + str(self.test_answer)
