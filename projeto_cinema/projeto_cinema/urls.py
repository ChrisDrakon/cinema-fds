
from django.urls import path
from app_cinema import views

urlpatterns = [
    path('',views.home,name='home'),
    path('cadastro/',views.cadastro,name='cadastro'),
]
