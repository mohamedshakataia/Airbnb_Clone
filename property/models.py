from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Room(models.Model):
    owner=models.ForeignKey(User,related_name='room_owner',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField(max_length=20000)
    location=models.ForeignKey('place',related_name='room_place',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photo/')
    category=models.ForeignKey('category',related_name='room_Category',on_delete=models.CASCADE)
    

    slug= models.SlugField(null=True ,blank=True)
    def save(self , *args ,**kwargs):
        if not self.slug:
            self.slug =slugify(self.name)
        super(Room, self).save(*args ,**kwargs)

    def get_absolute_url(self):
        return reverse('rooms:property_detail',kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    def check_avablity(self):
        all_avablities=self.room_book.all()
        now=timezone.now().date()
        for reserver in all_avablities :
            if now > reserver.to_date:
                return 'Available'
            elif now > reserver.from_date and now < reserver.to_date:
                return f'In Progress to {reserver.to_date} 12 PM'

        return 'Available'

    
    def get_avg_rating(self):
        all_review=self.room_review.all()
        ratting=0
        for review in all_review:
            ratting += review.rate

            return round(ratting /len(all_review),2)

        else:
            return '-'
    



class RoomImage(models.Model):
    room=models.ForeignKey(Room,related_name='room_image',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='room_image/')

    
    def __str__(self):
        return str(self.room)


    



class category(models.Model):
    name=models.CharField(max_length=60)
    icon=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= 'categories'



class RoomReview(models.Model):
    room=models.ForeignKey(Room,related_name='room_review',on_delete=models.CASCADE)
    author=models.ForeignKey(User,related_name='review_author',on_delete=models.CASCADE)
    rate=models.IntegerField()
    feedback=models.TextField(max_length=400)

    def __str__(self):
        return str(self.room)

    




class RoomBook(models.Model):
    room=models.ForeignKey(Room,related_name='room_book',on_delete=models.CASCADE)
    name=models.ForeignKey(User,related_name='user_book',on_delete=models.CASCADE)
    from_date=models.DateField(default=timezone.now)
    to_date=models.DateField(default=timezone.now)
    guest=models.IntegerField(default=1)
    children=models.IntegerField(default=0)


    def __str__(self):
        return str(self.name)


    def Inprogress(self):
        now=timezone.now().date()
        return now > self.from_date and now < self.to_date
    Inprogress.boolean=True



class place(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='place/')
    
    def __str__(self):
        return self.name