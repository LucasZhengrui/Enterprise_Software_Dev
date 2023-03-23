from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recovery/<int:dis_id>', views.recovery, name='recovery')
]