from django.shortcuts import render

from django.http import HttpResponse

from . import models

def index(request):

    query = models.Article.objects.all()

    return render(request, 'articles/index.htm', {'query': query})