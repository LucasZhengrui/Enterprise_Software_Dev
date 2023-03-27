from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # path('', views.index, name='index'),
    path('detail/<int:show_id>/', views.index, name='index'),
    path('update/<int:id>/', views.summary_edit, name='update')
]