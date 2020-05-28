from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Contact(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(default=None, max_length=10)
    message = models.TextField()

    def __str__(self):
        self.email
