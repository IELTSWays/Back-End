from django.db import models
from django.utils.html import format_html
from accounts.models import User
from datetime import datetime



class Teacher(models.Model):
    #id = models.IntegerField(primary_key=True,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=256,null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    photo = models.ImageField(upload_to='teachers',default="teachers/default.png")
    writing_price = models.IntegerField(default=0)
    speaking_price = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

    def cover(self):
        return format_html("<img width=40 src='{}'>".format(self.photo.url))




class ReserveTimes(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name="Teacher")
    time = models.DateTimeField()
    availabe = models.BooleanField(default=True)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.teacher.name) + ' | ' + str(self.time) + ' | ' + str(self.availabe) + ' | ' + str(self.reserved)
