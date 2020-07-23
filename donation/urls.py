from django.urls import path
from .views import donation

urlpatterns = [
    path('donation/', donation, name='donation'),

]
