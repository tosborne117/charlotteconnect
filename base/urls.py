from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('groups/<str:pk>/', views.group, name="groups"),
]
