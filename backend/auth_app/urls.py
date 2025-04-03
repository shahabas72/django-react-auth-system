from django.urls import path
from .views import register, login, logout, dashboard

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('dashboard/', dashboard),
]
