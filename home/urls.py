from django.urls import path, include
from . import views
from .views import PersonClassAPI, PeopleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person-vs', PeopleViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls)),

    path('index/', views.index),
    path('person-list/', views.person_list),
    path('person/add/', views.add_person),
    path('person/<int:pk>/', views.person),
    path('login/', views.login),
    path('person-api/', PersonClassAPI.as_view()),
]