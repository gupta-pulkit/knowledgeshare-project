from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects
    return render(request, 'blogs/home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})

@login_required(login_url = "/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            blog = Blog()
            blog.title = request.POST['title']
            blog.body = request.POST['body']
            blog.image = request.FILES['image']
            blog.pub_date = timezone.datetime.now()
            blog.author = request.user
            blog.save()
            return redirect('/blogs/'+str(blog.id))
        else:
            return render(request, 'blogs/create.html', {'error': "All fields are required"})
    else:
        return render(request, 'blogs/create.html')

@login_required(login_url = "/accounts/signup")
def like_blog(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk = blog_id)
        blog.likes_total += 1
        blog.save()
        return redirect('/blogs/'+str(blog.id))
