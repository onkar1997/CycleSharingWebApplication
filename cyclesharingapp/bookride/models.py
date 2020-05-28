from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Book(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None
    )
    pickup_location = models.CharField(max_length=50)
    drop_location = models.CharField(max_length=50)
    from_time = models.TimeField(auto_now=False, auto_now_add=False)
    to_time = models.TimeField(auto_now=False, auto_now_add=False)
    fare = models.IntegerField()
    book_date = models.DateField(
        auto_now=False, auto_now_add=False)

    def __str__(self):
        self.user.username
