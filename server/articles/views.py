from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from django.views.generic import View, CreateView, ListView, DetailView, UpdateView

from django.urls import reverse_lazy

from django.http import HttpResponse

from . import models
from . import forms

class ArticleList(ListView):
    context_object_name = 'query'
    
    template_name = 'articles/index.htm'

    queryset = get_list_or_404(models.Article)
    
class ArticleDetail(DetailView):
    model = models.Article

    context_object_name = 'instance'

    template_name = 'articles/detail.htm'

class ArticleCreate(CreateView):
    model = models.Article

    form_class = forms.ArticleForm

    success_url = reverse_lazy('articles:list')

    template_name = 'articles/edit.htm'

class ArticleUpdate(UpdateView):
    print('*'*50)
    
    model = models.Article

    form_class = forms.ArticleForm

    success_url = reverse_lazy('articles:detail')

    template_name = 'articles/edit.htm'