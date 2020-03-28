from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name = 'create'),
    path('<int:blog_id>/', views.detail, name = 'detail'),
    path('<int:blog_id>/like', views.like_blog, name = 'like_blog'),
]
