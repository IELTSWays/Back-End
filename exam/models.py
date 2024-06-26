from django.db import models
from book.models import Book
from exam.utils import random_N_chars_str
from accounts.models import User
from teacher.models import Teacher, ReserveTimes
import datetime
from django.utils import timezone


class TestPrice(models.Model):
    listening = models.IntegerField(default=0)
    reading = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.listening) + ' | ' + str(self.reading)




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
    confirm = models.BooleanField(default=False)
    confirm_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    full_report_paid = models.BooleanField(default=False)
    full_report_authority = models.CharField(max_length=128,null=True,blank=True)
    full_report_ref_id = models.CharField(max_length=128,null=True,blank=True)
    media_report_paid = models.BooleanField(default=False)
    media_report_authority = models.CharField(max_length=128, null=True, blank=True)
    media_report_ref_id = models.CharField(max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.test_id:
            self.test_id = random_N_chars_str(12)
        super(Test, self).save()

    def __str__(self):
        return str(self.skill) +'|'+ str(self.type) +'|'+ str(self.id)

    def is_expired(self):
        delta = timezone.now() - self.created_at
        delta_time_minutes = delta.total_seconds() / 60
        if self.skill == "listening" and delta_time_minutes >= 360:
            return True
        elif self.skill == "reading" and delta_time_minutes >= 480:
            return True
        else:
            return False





class SpeakingTest(models.Model):
    choices = (("new", "new"), ("pending", "pending"), ("canceled", "canceled"), ("paid", "paid"))
    status = models.CharField(choices=choices, default="new", max_length=128)
    test_id = models.CharField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=128,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_choices = (("academic","academic"),("general","general"))
    type = models.CharField(choices=type_choices, max_length=128)
    test_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    confirm = models.BooleanField(default=False)
    confirm_at = models.DateTimeField(null=True, blank=True)
    time = models.ForeignKey(ReserveTimes, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    description = models.CharField(max_length=255, null=True, blank=True)
    authority = models.CharField(max_length=36, null=True, blank=True)
    ref_id = models.IntegerField(null=True, blank=True)
    payment_choices = (("zibal", "zibal"), ("zarinpal", "zarinpal"), ("manual", "manual"))
    payment_method = models.CharField(choices=payment_choices, max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.test_id:
            self.test_id = random_N_chars_str(12)
        super(SpeakingTest, self).save()

    def __str__(self):
        return str(self.time) +'|'+ str(self.teacher) +'|'+ str(self.test_id)







class WritingTest(models.Model):
    choices = (("new", "new"), ("pending", "pending"), ("canceled", "canceled"), ("paid", "paid"))
    status = models.CharField(choices=choices, default="new", max_length=128)
    test_id = models.CharField(max_length=128, unique=True, blank=True)
    name = models.CharField(max_length=128,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_choices = (("academic","academic"),("general","general"))
    type = models.CharField(choices=type_choices, max_length=128)
    test_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    marker = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    confirm = models.BooleanField(default=False)
    confirm_at = models.DateTimeField(null=True, blank=True)
    score = models.IntegerField(default=0)
    task1 = models.TextField(max_length=2000,null=True,blank=True)
    task2 = models.TextField(max_length=2000, null=True, blank=True)
    amount = models.IntegerField(default=0)
    description = models.CharField(max_length=255, null=True, blank=True)
    authority = models.CharField(max_length=36, null=True, blank=True)
    ref_id = models.IntegerField(null=True, blank=True)
    payment_choices = (("zibal", "zibal"), ("zarinpal", "zarinpal"), ("manual", "manual"))
    payment_method = models.CharField(choices=payment_choices, max_length=128, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.test_id:
            self.test_id = random_N_chars_str(12)
        super(WritingTest, self).save()

    def __str__(self):
        return str(self.user) +'|'+ str(self.marker) +'|'+ str(self.test_id)

    def is_expired(self):
        delta = timezone.now() - self.created_at
        delta_time_minutes = delta.total_seconds() / 60
        if delta_time_minutes >= 480:
            return True
        else:
            return False





class TestHistory(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    band_score = models.CharField(max_length=128,null=True,blank=True)
    raw_score = models.CharField(max_length=128,null=True,blank=True)
    description = models.TextField(max_length=2500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.test) +'|'+ str(self.user) +'|'+ str(self.created_at)





class Note(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_choices = (("note","note"), ("highlight","highlight"))
    type = models.CharField(choices=type_choices, max_length=10)
    range = models.CharField(max_length=128,null=True,blank=True)
    note = models.CharField(max_length=256,null=True,blank=True)
    def __str__(self):
        return str(self.user) +'|'+ str(self.test) +'|'+ str(self.type)
