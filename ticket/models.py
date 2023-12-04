from django.db import models
from accounts.models import User

class Ticket(models.Model):
    STATUS=(('new','new'),('pending','pending'),('canceled','canceled'),('completed','completed'))
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(max_length=200, choices=STATUS, default='New')
    description = models.TextField(null=True,blank=True)
    answer = models.TextField(null=True,blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title) + "|" + str(self.user)

