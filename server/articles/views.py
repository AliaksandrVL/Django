from django.shortcuts import render, get_list_or_404

from django.http import HttpResponse

from . import models

def article_list(request):
    query = get_list_or_404(models.Article)

    return render(request, 'articles/index.htm', {'query': query})

def article_detail(request, pk):
    instance = get_list_or_404(models.Article, id=pk)

    return render(request, 'articles/detail.htm', {'instance': instance})