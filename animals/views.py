from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Animal


# Create your views here.
class AnimalListView(ListView):
    template_name = 'animals/animal_list.html'
    model = Animal


class AnimalDetailView(DetailView):
    template_name = 'animals/animal_detail.html'
    model = Animal


class AnimalCreateView(CreateView):
    template_name = 'animals/animal_create.html'
    model = Animal
    fields = ['title', 'purchaser', 'description']


class AnimalUpdateView(UpdateView):
    template_name = 'animals/animal_update.html'
    model = Animal
    fields = '__all__'


class AnimalDeleteView(DeleteView):
    template_name = 'animals/animal_delete.html'
    model = Animal
    success_url = reverse_lazy('animal_list')
