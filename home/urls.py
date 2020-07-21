from django.urls import path, include
from . import views

app_name = 'home'


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('rules/', views.rules, name="rules"),
    path('hello/', views.hello, name="hello"),
    path('base/', views.base, name="base"),


]
