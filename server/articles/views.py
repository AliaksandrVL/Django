from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    user = request.user

    return render(request, 'articles/index.html', {'content': 'Hello world!', 'user': user})