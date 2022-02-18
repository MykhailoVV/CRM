from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Job

# Create your views here.

class JobsListView(ListView):
    model = Job
    template_name = 'home.html'


class JobDetailView(DetailView):
    model = Job
    template_name = 'job_detail.html'

class JobCreateView(CreateView):
    model = Job
    template_name = 'job_new.html'
    fields = ['title', 'author', 'body']

class JobUpdateView(UpdateView):
    model = Job
    template_name = 'job_edit.html'
    fields = ['title', 'body']

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'job_delete.html'
    success_url = reverse_lazy('home')