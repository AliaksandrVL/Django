from django.urls import path

from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.CategoryList.as_view(), name='list'),
    path('<int:pk>/', views.CategoryDetail.as_view(), name='detail')
]
