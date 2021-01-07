from django.contrib import admin
from .models import Post , category
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin,admin.ModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Post,PostAdmin)


admin.site.register(category)

