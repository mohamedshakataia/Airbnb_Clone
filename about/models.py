from django.db import models

# Create your models here.



class About(models.Model):
    what_we_do=models.TextField(max_length=1500)
    goal=models.TextField(max_length=1500)
    mission=models.TextField(max_length=1500)
    image=models.ImageField(upload_to='photo/')



    def __str__(self):
        return str(self.id)


    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class FAQ(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField(max_length=1500)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQS'

    
