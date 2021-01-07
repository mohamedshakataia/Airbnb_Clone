from django.shortcuts import render
from property.models import place ,Room ,category
from django.db.models import Q , Count
from django.contrib.auth.models import User
from blog.models import Post
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.






def Home(request):
    places=place.objects.all().annotate(place_categroy=Count('room_place'))
    categories=category.objects.all()
    Users_count=User.objects.all().count()
    place_count=place.objects.all().count()
    hotal_count=Room.objects.filter(category__name='Hotel').count()
    Restaurant_count=Room.objects.filter(category__name='Restaurant').count()
    latest_posts = Post.objects.all()[:4]
    Popular_Restaurants=Room.objects.filter(category__name='Restaurant')
    Popular_hotel=Room.objects.filter(category__name='Hotel')
    Popular_shopping=Room.objects.filter(category__name='Shopping')

    return render(request,'setting/home.html',{
        'places':             places ,
        'categories':         categories ,
        'Users_count':        Users_count,
        'place_count':        place_count ,
        'hotal_count':        hotal_count ,
        'Restaurant_count':   Restaurant_count ,
        'latest_posts':       latest_posts ,
        'Popular_Restaurants':Popular_Restaurants,
        'Popular_hotel':      Popular_hotel,
        'Popular_shopping':    Popular_shopping ,
        })



def home_search(request):
    name=request.GET.get('q')  
    place=request.GET.get('place') 
    search_result= Room.objects.filter(
        Q(name__icontains=name)&
        Q(location__name__icontains=place)
    )
    return render(request,'setting/search.html',{'search_result':search_result})


def filter_by_category(request,name_category):
    properties=Room.objects.filter(category__name=name_category)
    return render(request,'setting/search.html',{'search_result':properties})


def contact(request):
    info =Info.objects.last()
    if request.method=='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Subject=request.POST['subject']
        Message=request.POST['message']
        send_mail(
            Subject,
            f'Message From : {Name} \n Email : {Email} \n Message : {Message}',
            Email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
            )

    return render(request,'setting/contact.html',{
        'info':info
        })


