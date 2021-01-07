from django.urls import path
from . import views
from .api_view import Roomlistview , RoomDetailview

app_name='property'


urlpatterns = [
    path('',views.RoomList.as_view(),name='property_list'),
    path('NewRoom',views.NewRoom.as_view(),name='NewRoom'),
    path('<slug>',views.RoomDetail.as_view(),name='property_detail'),


    path('api/list',Roomlistview.as_view(),name='Roomlistview'),
    path('api/list/<int:pk>',RoomDetailview.as_view(),name='RoomDetailview'),

]
