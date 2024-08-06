from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_de_atividades, name='lista_de_atividades'),
]