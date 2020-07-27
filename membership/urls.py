from django.contrib import admin
from django.urls import path, include
from .views import membership,  stripee, stripee_two, chargeCustomer, create_donation, donation
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('membership/', membership, name='membership'),
    path('stripee/', stripee, name='stripee'),
    path('stripee_two/', stripee_two, name='stripee_two'),
    path('charge/', chargeCustomer, name='charge'),
    path('donate/', create_donation, name='donate'),
    path('donation/', donation, name='donation'),
]
