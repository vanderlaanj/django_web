from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from .models import Sportovec, Tym, Akce
# Create your views here.

def index(request):
    return render(request, 'index.html')

class SportovecDetail(DetailView):
    model = Sportovec
    template_name = 'sportovec/sportovec_detail.html'
    context_object_name = 'sportovec'

class SportovecList(ListView):
    model = Sportovec
    template_name = 'sportovec/sportovec_list.html'
    context_object_name = 'sportovci'
    ordering = ['prijmeni']

class AkceDetail(DetailView):
    model = Akce
    template_name = 'akce/akce_detail.html'
    context_object_name = 'akce'

class AkceList(ListView):
    model = Akce
    template_name = 'akce/akce_list.html'
    context_object_name = 'akce'