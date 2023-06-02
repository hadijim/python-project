from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
import uuid
import datetime


# Create your models here

class CustomUser(AbstractUser):
    username = None
    codepersonely = models.BigIntegerField(unique=True)
    is_warekeeper = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)

    USERNAME_FIELD = "codepersonely"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.codepersonely)


class Good(models.Model):
    name = models.CharField(max_length=50)
    ma_data = models.DateField()
    exp_data = models.DateField()
    num = models.IntegerField()
    company_price = models.IntegerField()
    consumer_price = models.IntegerField()

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    discount = models.CharField(max_length=100, blank=True, null=True)
    discount_start_date = models.DateField(blank=True, null=True)
    discount_end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.user.codepersonely)


class Factor(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT)
    good = models.ForeignKey(Good, on_delete=models.PROTECT)

    def __str__(self):
        return self.pk
