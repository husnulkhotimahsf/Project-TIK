from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faperta/', views.faperta, name='faperta'),
    path('fh/', views.fh, name='fh'),
    path('fkip/', views.fkip, name='fkip'),
    path('ft/', views.ft, name='ft'),
    path('feb/', views.feb, name='feb'),
    path('fisip/', views.fisip, name='fisip'),
    path('fk/', views.fk, name='fk'),
    path('pascasarjana/', views.pascasarjana, name='pascasarjana'),
]