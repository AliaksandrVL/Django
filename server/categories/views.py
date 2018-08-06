from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from django.views.generic import View, CreateView, ListView, DetailView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from . import models

class CategoryList(ListView):
    context_object_name = 'query'
    template_name = 'categories/index.htm'
    queryset = get_list_or_404(models.Category)
    
class CategoryDetail(DetailView):
    model = models.Category
    context_object_name = 'instance'
    template_name = 'categories/detail.htm'