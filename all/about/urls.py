
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', about , name='about' ),
]