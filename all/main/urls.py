from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('success/', error, name='error'),
    path('filter/', filter_data, name='filter_data'),
    path('loading/<int:num_posts>/', loadding, name='loading'),




]
