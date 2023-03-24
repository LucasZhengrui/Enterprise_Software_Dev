from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('message_submit/', views.message_submit, name='message_submit'),
]