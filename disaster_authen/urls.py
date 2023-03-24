from django.urls import path
from . import views
from .views import user_list

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('user/', views.user_list, name='userlist')

]