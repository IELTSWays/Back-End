from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=60,unique=True)

    def __str__(self):
        return str(self.name)


class City(models.Model):
    province = models.ForeignKey(Province,on_delete=models.CASCADE)
    name = models.CharField(max_length=256,unique=True)

    def __str__(self):
        return str(self.name)
