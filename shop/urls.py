"""pramit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header='NutriHub'
admin.site.site_title='NutriHub'

urlpatterns = [
    path('shop/home/', views.index),
    path('', views.lo),
    path('login/', views.login),
    path('shop/contact/', views.contact),
    path('shop/reg/', views.register),
    path('shop/tracking/', views.tracking),
    path('shop/myorderf/', views.order),
    path('shop/cart/', views.cart),
    path('shop/products/<int:id>', views.product, name="prod"),
    path('shop/delete/<int:id>', views.delete, name="prod"),
 path('shop/products/<int:id>', views.products, name="prod"),
  path('shop/cat/<str:m>', views.search, name="prod"),
  path('shop/searchu', views.searchu, name="prod"),
   path('shop/filter', views.searchuu, name="prod"),
    path('shop/shop/', views.shop),
 path('shop/checkout/', views.checkout),
path('shop/orderNow/', views.orderNow),
path('shop/login/', views.login),
path('shop/review/', views.review),
path('shop/check/', views.check),
]
