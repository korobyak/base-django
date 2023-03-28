from django.urls import path

from src.users.views import login, registration, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registartion/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),

]

