from django.urls import path

from . import endpoints
from . import views

app_name = 'articles'

endpoints = [
    path('api/', endpoints.api_product_list, name='api_list')
]

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('create/', views.ArticleCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ArticleUpdate.as_view(), name='update'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail')
] + endpoints
