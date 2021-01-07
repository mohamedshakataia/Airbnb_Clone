from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class RoomImagesTabular(admin.TabularInline):
    model = models.RoomImage


class RoomAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    list_display= ['name','price','location' ,'get_avg_rating','check_avablity']
    inlines=[RoomImagesTabular,]
    summernote_fields = ('description',)
    prepopulated_fields = {'slug':("name",)}




admin.site.register(models.Room,RoomAdmin)
# admin.site.register(models.RoomImage)
admin.site.register(models.category)
admin.site.register(models.RoomReview)

class RoomBookAdmin(admin.ModelAdmin):
    list_display= ['room','Inprogress' ]
   
admin.site.register(models.RoomBook,RoomBookAdmin)
admin.site.register(models.place)



