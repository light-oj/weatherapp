from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.my_search, name="my-search"),
]
