from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Zones(models.Model):
    name=models.CharField(max_length=30)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zone = models.OneToOneField(Zones, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    salary=models.IntegerField()

    def retrive(user):
        profile=Profile.objects.get(user=user)
        return profile

class Products(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.CharField(max_length=300, blank=True)

    def addNewProduct(name,price,description):
        p = Products(name=name, price=price,description=description)
        p.save()

    def viewProducts():
        return Products.objects.all()

class StockManager(models.Model):
    product=models.OneToOneField(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField()


class Orders(models.Model):
    product=models.OneToOneField(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    zone=models.OneToOneField(Zones, on_delete=models.CASCADE)
    retailer=models.CharField(max_length=300)

class Sales(models.Model):
    product=models.OneToOneField(Products, on_delete=models.CASCADE)
    zone=models.OneToOneField(Zones, on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=True)


