from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/', views.signup, name='signup'),
]