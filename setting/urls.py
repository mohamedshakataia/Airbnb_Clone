from django.urls import path
from . import views


app_name='setting'

urlpatterns=[
    path('', views.Home ,name='Home'),
    
    path('search/', views.home_search ,name='home_search'),
    path('contact/', views.contact ,name='contact'),
    path('<str:name_category>/', views.filter_by_category ,name='filter_by_category'),


]