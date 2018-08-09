from django.urls import path

from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.CategoryList.as_view(), name='list'),
    path('create/', views.CategoryCreate.as_view(), name='create'),
    path('<int:pk>/', views.CategoryDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.CategoryUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.CategoryDelete.as_view(), name='delete')
]
