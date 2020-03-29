from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name = 'create'),
    path('category/<int:blog_id>/', views.detail, name = 'detail'),
    path('<str:cat>/', views.category, name = 'category'),
    path('<int:blog_id>/like', views.like_blog, name = 'like_blog'),
]
