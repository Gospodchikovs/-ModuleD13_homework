from django.shortcuts import render
from django.views.generic import ListView
from .models import Advertisment


class AdvertismentList(ListView):
    model = Advertisment
    template_name = 'advertisment.html'
    context_object_name = 'advertisments'
    ordering = '-time_create'
