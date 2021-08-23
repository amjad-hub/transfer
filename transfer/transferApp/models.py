from django.db import models
from django.contrib.auth.models import User
#Create your models here.


class user_account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TIN = models.PositiveBigIntegerField(unique=True)
    invoice = models.DecimalField(max_digits=100, decimal_places=1)

    def __str__(self):
        return f'{self.user.username} Account'


class transfer(models.Model):
    transfer_From = models.PositiveBigIntegerField(default=1)
    transfer_To_TIN = models.CharField(max_length=400)
    amount_money = models.DecimalField(max_digits=100, decimal_places=1)


