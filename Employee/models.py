from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zone = models.CharField(max_length=30, blank=True)
    dob = models.DateField(null=True, blank=True)
    salary=models.IntegerField()

    def retrive(user):
        profile=Profile.objects.get(user=user)
        return profile
