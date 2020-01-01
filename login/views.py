from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse

# Create your views here.
def user_login(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == 'POST':
        # user = users(request.POST)
        username = request.POST.get('UserName')
        password = request.POST.get('password')
        typeOf = request.POST.get('type')
        user=authenticate(request,username=username,password=password)
        if user:
            usr_group = user.groups.values_list('name',flat = True)
            print(usr_group[0])
            if(typeOf == 'ZoneSalesManager' and usr_group[0]==typeOf):
                login(request,user)
                return HttpResponseRedirect("/Employee/ZoneSalesManager")
                # render(request,'GM/index.html',{'userName': user, 'type':typeOf})        
            if(typeOf == 'NationalSalesManager' and usr_group[0]==typeOf):
                login(request,user)
                return HttpResponseRedirect("/Employee/NationalSalesManager")
            if(typeOf == 'ProductSalesManager' and usr_group[0]==typeOf):
                login(request,user)
                return HttpResponseRedirect("/Employee/ProductSalesManager")      
            if(typeOf == 'SalesForce' and usr_group[0]==typeOf):
                login(request,user)
                return HttpResponseRedirect("/Employee/SalesForce")   
        else:
            return render(request,'login/login.html')
        # userName = users(request.POST)
        
    else:
        return render(request,'login/login.html')