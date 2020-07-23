from django.contrib import admin
from django.urls import path, include
from .views import  membership,  stripee, chargeCustomer
from django.contrib.auth import views as auth_views


urlpatterns = [


    path('membership/', membership, name='membership'),
    path('stripee/', stripee, name='stripee'),
    path('charge/', chargeCustomer, name='charge'),
]
