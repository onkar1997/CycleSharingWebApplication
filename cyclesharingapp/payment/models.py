from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Pay(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )
    username = models.CharField(max_length=50)
    cardNumber = models.CharField(max_length=50)
    cardExpiry = models.CharField(max_length=50)
    cardCv = models.CharField(max_length=50)
    cardHolder = models.CharField(max_length=50)
    totalAmount = models.CharField(max_length=50)

    def __str__(self):
        self.cardHolder
