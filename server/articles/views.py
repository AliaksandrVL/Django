from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from django.views.generic import View, CreateView, ListView, DetailView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from . import models
from . import forms

class ArticleList(ListView):
    context_object_name = 'query'
    template_name = 'articles/index.htm'
    queryset = get_list_or_404(models.Article)
    paginate_by = 1
    
class ArticleDetail(DetailView):
    model = models.Article
    context_object_name = 'instance'
    template_name = 'articles/detail.htm'

class ArticleCreate(LoginRequiredMixin, CreateView):
    model = models.Article
    form_class = forms.ArticleForm
    success_url = reverse_lazy('articles:list')
    login_url = reverse_lazy('security:login')
    template_name = 'articles/edit.htm'

class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = models.Article
    form_class = forms.ArticleForm
    success_url = reverse_lazy('articles:detail')
    login_url = reverse_lazy('security:login')
    template_name = 'articles/edit.htm'