from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('logout/', views.logout_view),
    path('createBracket/', views.createBracket),
    path('brackets/', views.get_brackets),
    path('tournaments/<int:page>/', views.postedTournament, name='room'),
]