from django.urls import path
# Importing views from current directory "."
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prices', views.prices, name='prices'),
]
 