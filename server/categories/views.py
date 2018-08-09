from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from . import models
from . import forms

class CategoryList(LoginRequiredMixin, ListView):
    context_object_name = 'query'
    login_url = reverse_lazy('security:login')
    template_name = 'categories/index.htm'
    queryset = get_list_or_404(models.Category)
    
class CategoryDetail(LoginRequiredMixin, DetailView):
    model = models.Category
    context_object_name = 'instance'
    login_url = reverse_lazy('security:login')
    template_name = 'categories/detail.htm'

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = models.Category
    form_class = forms.CategoryForm
    success_url = reverse_lazy('categories:list')
    login_url = reverse_lazy('security:login')
    template_name = 'categories/edit.htm'

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    success_url = reverse_lazy('categories:list')
    login_url = reverse_lazy('security:login')
    template_name = 'categories/edit.htm'

class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = models.Category
    form_class = forms.CategoryForm
    success_url = reverse_lazy('categories:list')
    login_url = reverse_lazy('security:login')
    template_name = 'categories/delete.htm'