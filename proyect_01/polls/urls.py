from django.urls import path
from polls.views import mensaje,potencia,func_num,home

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mensaje/', views.mensaje, name='mensaje'),
    path('potencia/<int:valor>', views.potencia ,name='potencia'),
    path('number/<str:valors>', views.func_num ,name='number'),
    path('home/',views.home,name='home'),

]