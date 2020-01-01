from django.urls import path

from . import views

urlpatterns = [
    path('ZoneSalesManager', views.ZoneSalesManager.as_view(), name='ZoneSalesManager'),
    path('NationalSalesManager', views.NationalSalesManager.as_view(), name='NationalSalesManager'),
    path('ProductManager', views.ProductManager.as_view(), name='ProductManager'),
    path('SalesForce', views.SalesForce.as_view(), name='SalesForce'),
]

