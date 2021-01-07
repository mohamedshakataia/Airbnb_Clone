from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile
from .forms import userform , Profileform , UseCreateForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from property.models import RoomBook ,Room
from property.forms import RoomReviewForm
# Create your views here.


def signup(request):
    if request.method =='POST':
        signup_form = UseCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            #return redirect(reverse('login'))                  ### signup and reverse to login page
            username = signup_form.cleaned_data['username']     ### update session
            password = signup_form.cleaned_data['password1']
            user     = authenticate(username=username , password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))      ### signup and reverse to profile page
    else:
        signup_form = UseCreateForm()
    return render (request , 'registration/signup.html' , {'signup_form':signup_form})    
        

def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render (request , 'profile/profile.html' , {'profile':profile})


def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method =='POST':
        user_form    = userform(request.POST ,instance=request.user)
        Profile_form = Profileform(request.POST ,request.FILES , instance=profile)

        if user_form.is_valid() and Profile_form.is_valid():
            user_form.save()
            my_form = Profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            return redirect(reverse('accounts:profile'))

    else:
        user_form    = userform(instance=request.user)
        Profile_form = Profileform(instance=profile)
    

    return render (request , 'profile/profile_edit.html' ,{'user_form':user_form ,'Profile_form':Profile_form})



def user_reservation(request):
    myreservation=RoomBook.objects.filter(name=request.user)
    return render(request, 'profile/MyReservation.html',{'myreservation':myreservation})

def MyRoom(request):
    MyRooms=Room.objects.filter(owner=request.user)
    return render(request, 'profile/MyRoom.html',{'MyRooms':MyRooms})




def feedback(request,slug):
    room=get_object_or_404(Room ,slug=slug)
    if request.method == 'POST':
        form=RoomReviewForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.room=room
            myform.author=request.user
            myform.save()
            return redirect(reverse('rooms:property_detail',kwargs={'slug': room.slug}))
    else:
        form=RoomReviewForm()   
    return render(request,'profile/add_review.html',{'form':form})
