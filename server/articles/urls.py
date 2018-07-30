from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('create/', views.ArticleCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ArticleUpdate.as_view(), name='update'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail')
]
