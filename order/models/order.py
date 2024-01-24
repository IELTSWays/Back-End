from accounts.models import User
from django.db import models
from accounts.utils import random_N_chars_str
from exam.models import Test


class Order(models.Model):
    order_id = models.CharField(max_length=255, null=True, blank=True)
    choices = (("new", "new"), ("pending", "pending"), ("canceled", "canceled"), ("paid", "paid"))
    status = models.CharField(choices=choices, default="new", max_length=128)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    test = models.ManyToManyField(Test)
    authority = models.CharField(max_length=36, null=True, blank=True)
    ref_id = models.IntegerField(null=True,blank=True)
    payment_choices = (("zibal","zibal"),("zarinpal","zarinpal"),("manual","manual"))
    payment_method = models.CharField(choices=payment_choices,max_length=128,null=True,blank=True)


    def __str__(self):
        return str(self.order_id) +'|'+ str(self.user) +'|'+ str(self.status)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = random_N_chars_str(12)
        super(Order, self).save()





class ManualPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    transaction_number = models.CharField(max_length=255, null=True, blank=True)
    transaction_photo = models.ImageField(upload_to='transaction',null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
