from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Room ,  RoomReview
from .Serializer import RoomSerializers ,RoomReviewSerializers
from rest_framework.generics import ListAPIView ,RetrieveAPIView ,CreateAPIView ,UpdateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view




class Roomlistview(ListAPIView ,CreateAPIView):
    model= Room
    serializer_class=RoomSerializers
    queryset= Room.objects.all()
    permission_classes=[IsAuthenticated]




class RoomDetailview(RetrieveUpdateDestroyAPIView):
    model= Room
    serializer_class=RoomSerializers
    queryset=Room.objects.all()
    permission_classes=[IsAuthenticated]


