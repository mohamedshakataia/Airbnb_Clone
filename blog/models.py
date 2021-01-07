from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=50)
    tags = TaggableManager()
    image=models.ImageField(upload_to='photo/',null=True , blank=True)
    create_at=models.DateField(default=timezone.now)
    author=models.ForeignKey(User,related_name='post_authar',on_delete=models.CASCADE)
    viewcount=models.IntegerField(default=0)
    category=models.ForeignKey('category',related_name='post_Category',on_delete=models.CASCADE)
    description=models.TextField(null=True , blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk': self.pk})



 
class category(models.Model):
    name=models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= 'categories'  

    