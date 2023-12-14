from accounts.models import User
from django.db import models
from cart.models import Order
from accounts.utils import random_N_chars_str


class Transaction(models.Model):
    transaction_id = models.CharField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True)
    authority = models.CharField(max_length=36, null=True, blank=True)
    ref_id = models.IntegerField(null=True, blank=True)
    success = models.BooleanField(default=False)

    def __str__(self):
        return str(self.transaction_id) +'|'+ str(self.user)

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = random_N_chars_str(12)
        super(Transaction, self).save()

