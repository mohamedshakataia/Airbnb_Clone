from django.shortcuts import render ,reverse ,redirect
from . import models
from django.views.generic import DetailView ,CreateView
from django_filters.views import FilterView
from .fillter import propertyFilter
from django.views.generic.edit import FormMixin
from .forms import RoomBookForm
from django.urls import reverse 
# Create your views here.



class RoomList(FilterView):
    model=models.Room
    filterset_class = propertyFilter
    template_name= 'property/room_list.html'
    paginate_by = 6
    


class RoomDetail(FormMixin,DetailView):
    model=models.Room
    form_class = RoomBookForm
    success_url = '/rooms/' 
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_property"] = models.Room.objects.filter(category=self.get_object().category)
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            myform=form.save(commit=False)
            myform.room = self.object
            myform.save()
        return redirect(reverse('rooms:property_detail',kwargs={'slug': self.object.slug}))




class NewRoom(CreateView):
    model=models.Room
    fields=['name','price','description','location','image','category']

    def post(self, request, *args, **kwargs):
        form=self.get_form()
        if form.is_valid():
            myform= form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('rooms:property_list'))
        


            

