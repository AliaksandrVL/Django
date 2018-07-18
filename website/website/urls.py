"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
import mainapp.views as views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^articles/', views.articles),
    url(r'^article_SiJava/', views.article_SiJava, name = 'Java'),
    url(r'^article_Pattaya/', views.article_Pattaya, name = 'Pattaya'),
    url(r'^contacts/', views.contacts),
    url(r'^admin/', admin.site.urls),
]
