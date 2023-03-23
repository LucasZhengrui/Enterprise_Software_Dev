from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.index, name='search'),
    path('delete/<int:dis_id>/', views.delete, name='delete'),
    path('download/<int:page_id>/<str:search_field>/<str:search_query>/', views.download, name='download'),   
]