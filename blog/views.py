from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post ,category
from taggit.models import Tag
from django.db.models import Count ,Q
# Create your views here.



class postview(ListView):
    model=Post
    paginate_by = 3


    def get_queryset(self):
        name=self.request.GET.get('q','')
        object_list=Post.objects.filter(
            Q(title__icontains=name)|
            Q(description__icontains=name)
        )

        return object_list




class PostDetail(DetailView):
    model=Post

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resent_post"] = Post.objects.all()[:3]
        context["categroies"] = category.objects.all().annotate(post_count=Count('post_Category'))
        context["tags"] = Tag.objects.all()
        return context



