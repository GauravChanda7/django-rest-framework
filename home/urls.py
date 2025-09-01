from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('person-list/', views.person_list),
    path('person/<int:pk>/', views.person),
    path('person/add/', views.add_person),
    path('login/', views.login),
]