from django.urls import path
from toys.views import *

urlpatterns = [
    path('toy_list/', toy_list, name='toy_list'),
    path('toy_detail/<int:pk>/', toy_detail, name='toy_detail'),
]