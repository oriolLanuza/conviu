from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:profile>/', views.profile, name='profile'),
    path('profile/<str:profile>/addevent/', views.addevent, name='addevent'),
]