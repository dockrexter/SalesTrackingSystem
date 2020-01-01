from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
from datetime import date
from . import order


# Create your views here.

class Employee:
    name=""
    dob=date.today()
    age=22
    email="abcd@gmail.com"
    salary=1234

    def getdata(self):
        print(self.name,self.dob,self.email,self.salary)


class ZoneSalesManager(View,Employee):
    ZoneSalesManager = Employee()
    def get(self,request):
        if(request.user):
            user=request.user
            ZoneSalesManager.name=user.username
            profile=Profile.retrive(user)
            ZoneSalesManager.dob=profile.dob
            ZoneSalesManager.salary=profile.salary
            ZoneSalesManager.age=((date.today())-(Employee.dob))
            usr_group = request.user.groups.values_list('name',flat = True)
            username=request.user.username
            ZoneSalesManager.getdata(ZoneSalesManager)
            context={'username':username}
            if(usr_group[0]=="ZoneSalesManager"):
                return render(request,'Zone/ZoneSalesManager.html',context)
            else:
                return HttpResponseRedirect("/login")
        else:
            return HttpResponseRedirect("/login")


class NationalSalesManager(View,Employee):   
    def get(self,request):
        if(request.user):
            usr_group = request.user.groups.values_list('name',flat = True)
            if(usr_group[0]=="NationalSalesManager"):
                return render(request,'Zone/NationalSalesManager.html')
            else:
                return HttpResponseRedirect("/login")
        else:
            return HttpResponseRedirect("/login")

class ProductManager(View,Employee):   
    def get(self,request):
        if(request.user):
            usr_group = request.user.groups.values_list('name',flat = True)
            if(usr_group[0]=="ProductManager"):
                product=Products.viewProducts()
                context={"product":product}
                return render(request,'Zone/ProductManager.html',context)
            else:
                return HttpResponseRedirect("/login")
        else:
            return HttpResponseRedirect("/login")

    def addNewProduct(request):
        if request.method == 'POST':
            Products.addNewProduct(request.POST["name"],request.POST["price"],request.POST["description"])
            return HttpResponseRedirect("/Employee/ProductManager")
        else:
            return HttpResponse("hello")
        # return HttpResponse("hello")

class SalesForce(View,Employee):   
    def get(self,request):
        if(request.user):
            usr_group = request.user.groups.values_list('name',flat = True)
            if(usr_group[0]=="SalesForce"):
                return render(request,'Zone/SalesForce.html')
            else:
                return HttpResponseRedirect("/login")
        else:
            return HttpResponseRedirect("/login")
