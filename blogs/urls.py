from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name = 'create'),
    path('detail/<int:blog_id>/', views.detail, name = 'detail'),
    path('category/<str:cat>/', views.category, name = 'category'),
    path('<int:blog_id>/like', views.like_blog, name = 'like_blog'),
    path('myposts/', views.myposts, name = 'myposts'),
    path('delete/<int:blog_id>/', views.delete, name = 'delete'),
]
