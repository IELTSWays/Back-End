from django.db import models
from exam.models import Test
from accounts.models import User
from book.models import Book
from ckeditor.fields import RichTextField



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
    full_answer = RichTextField(max_length=7000, null=True, blank=True)

    def __str__(self):
        return str(self.answer) + ' | ' + str(self.test_answer)







class TestMediaAnswer(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    skill_choices = (("listening", "listening"), ("reading", "reading"), ("writing", "writing"))
    skill = models.CharField(choices=skill_choices, max_length=128)
    type_choices = (("academic", "academic"), ("general", "general"))
    type = models.CharField(choices=type_choices, max_length=128)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) +'|'+ str(self.book)




class MediaAnswer(models.Model):
    test_answer = models.ForeignKey(TestMediaAnswer,on_delete=models.CASCADE)
    question_number = models.IntegerField()
    video = models.FileField(upload_to='video_answer')
    audio = models.FileField(upload_to='audio_answer')

    def __str__(self):
        return str(self.test_answer) + ' | ' + str(self.question_number)
