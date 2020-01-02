from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date

class Zones(models.Model):
    name=models.CharField(max_length=30)
    
    def viewZones():
        return Zones.objects.all()

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
        return p

    def viewProducts():
        return Products.objects.all()


class StockManager(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def addNewProduct(name,price,description):
        p=Products.addNewProduct(name,price,description)
        t=StockManager(product=p,quantity=0)
        t.save()
    
    def viewProducts():
        return Products.viewProducts()
        
    def addStock(quantity,product):
        s = StockManager.objects.get(product_id=product)
        s.quantity += int(quantity)  # change field
        s.save() # this will update only
    
    def viewStock():
        return StockManager.objects.all()


class Orders(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    zone=models.ForeignKey(Zones, on_delete=models.CASCADE)
    retailer=models.CharField(max_length=300)

    def viewStock():
        return StockManager.viewStock()

    def ViewZones():
        return Zones.viewZones()

    def bookOrder(name,quantity,zone,retailer):
        p = Products.objects.get(name=name)
        z = Zones.objects.get(name=zone)
        b = Orders(product=p,quantity=quantity,zone=z,retailer=retailer)
        b.save();

    def viewOrders(zone):
        return Orders.objects.filter(zone=zone)

    def getOrder(id):
        return Orders.objects.get(id=id)
        




class Sales(models.Model):
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    zone=models.ForeignKey(Zones, on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=True)
    date = models.DateField(auto_now=True,auto_now_add=False)

    def addSales(product,zone,quantity):
        s=Sales(product=product,zone=zone,quantity=quantity)
        s.save()



