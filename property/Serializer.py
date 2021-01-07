from rest_framework import serializers
from .models import Room ,RoomReview


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=['owner','name','price','description','location','image','category']



class RoomReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model=RoomReview
        fields=['room','rate','feedback']

