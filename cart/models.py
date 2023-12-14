from accounts.models import User
from django.db import models
from book.models import Book
from accounts.utils import random_N_chars_str



class Order(models.Model):
    choices = (("new","new"),("canceled","canceled"),("paid","paid"))
    status = models.CharField(choices=choices,default="new",max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=128,unique=True,blank=True)
    books = models.ManyToManyField(Book)
    total_price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    @property
    def products_count(self):
        return self.books.count()

    def __str__(self):
        return str(self.order_id)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = random_N_chars_str(12)
        super(Order, self).save()


