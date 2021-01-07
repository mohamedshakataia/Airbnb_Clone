from django import forms
from .models import RoomBook ,RoomReview

class RoomBookForm(forms.ModelForm):
    from_data = forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    to_data = forms.DateField(widget=forms.DateInput(attrs={'id':'checkin_date'}))
    class Meta:
        model=RoomBook
        exclude = ['room',]




class RoomReviewForm(forms.ModelForm):
    class Meta:
        model=RoomReview
        fields=['rate','feedback',]