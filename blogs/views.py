from django.shortcuts import render

def home(request):
    return render(request, 'blogs/home.html')

def create(request):
    return render(request, 'blogs/create.html')
