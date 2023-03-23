from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.index, name='search'),
    path('delete/<int:dis_id>/', views.delete, name='delete'),  
]