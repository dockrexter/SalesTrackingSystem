from django.urls import path

from . import views

urlpatterns = [
    path('ZoneSalesManager', views.ZoneSalesManager.as_view(), name='ZoneSalesManager'),
    path('NationalSalesManager', views.NationalSalesManager.as_view(), name='NationalSalesManager'),
    path('ProductManager', views.ProductManager.as_view(), name='ProductManager'),
    path('ProductManager/addNewProduct', views.ProductManager.addNewProduct, name='ProductManager'),
    path('ProductManager/addStock', views.ProductManager.addStock, name='addStock'),
    path('SalesForce', views.SalesForce.as_view(), name='SalesForce'),
]

