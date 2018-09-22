from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=128)
    date = models.DateTimeField(auto_now=True)
    cost = models.IntegerField(null=True)
    mileage = models.BigIntegerField(null=True)

