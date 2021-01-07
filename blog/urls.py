from django.urls import path
from .views import postview , PostDetail
from .api_view import post_list_api ,post_detail_api ,post_search_api


app_name='blog'

urlpatterns = [
    path('',postview.as_view() ,name='blog'),
    path('<int:pk>',PostDetail.as_view() ,name='detail'),



    path('api/list', post_list_api ,name='api_list'),
    path('api/list/<str:q>', post_search_api ,name='post_search_api'),
    path('api/list/<int:pk>', post_detail_api ,name='post_detail_api'),
   
]