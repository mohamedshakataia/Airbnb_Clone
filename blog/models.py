from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Post(models.Model):
    title=models.CharField(_('title'),max_length=50)
    tags = TaggableManager(_('tags'))
    image=models.ImageField(_('image'),upload_to='photo/',null=True , blank=True)
    create_at=models.DateField(_('create_at'),default=timezone.now)
    author=models.ForeignKey(User,related_name='post_authar',on_delete=models.CASCADE,verbose_name='author')
    viewcount=models.IntegerField(_('viewcount'),default=0)
    category=models.ForeignKey('category',related_name='post_Category',on_delete=models.CASCADE,verbose_name='category')
    description=models.TextField(_('description'),null=True , blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk': self.pk})



 
class category(models.Model):
    name=models.CharField(_('name'),max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= 'categories'  

    