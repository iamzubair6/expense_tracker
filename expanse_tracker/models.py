from django.db import models
from datetime import datetime, date
# Create your models here.


class Type(models.Model):
    Type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.Type}'


class Expanse(models.Model):

    Type = models.OneToOneField(
        Type, on_delete=models.CASCADE, related_name='expanse_type')
    Amount = models.FloatField(max_length=50, null=True)
    Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.Type} {self.Amount}'
