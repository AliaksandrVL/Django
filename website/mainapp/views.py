from django.shortcuts import render

def main(request):
    return render(request, 'mainapp/index.html')

def articles(request):
    return render(request, 'mainapp/articles.html')

def article_Pattaya(request):
    return render(request, 'mainapp/articles/article_Pattaya.html')

def article_SiJava(request):
    return render(request, 'mainapp/articles/article_SiJava.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')
