from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from models import sportovec, tym, akce
# Create your views here.

class index(ListView):
    template_name = 'tempelates/index.html'

class SportovecDetail(DetailView):
    model = sportovec
    template_name = 'tempelate/sportovec_detail.html'
    context_object_name = 'sportovec'

class SportovecList(ListView):
    model = sportovec
    template_name = 'tempelates/sportovec_list.html'
    context_object_name = 'sportovci'
    ordering = ['prijmeni']

class AkceDetail(DetailView):
    model = akce
    template_name = 'tempelates/akce_detail.html'
    context_object_name = 'akce'

class AkceList(ListView):
    model = akce
    template_name = 'tempelates/akce_list.html'
    context_object_name = 'akce'