from django.urls import path, include
from . import views
from .views import PersonClassAPI, PeopleViewSet, RegisterAPIUser, LoginAPIUser
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
    
    path('user/register/', RegisterAPIUser.as_view()),
    path('user/login/', LoginAPIUser.as_view()),
    path('user/person-api/', PersonClassAPI.as_view()),
]