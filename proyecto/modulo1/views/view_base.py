from django.shortcuts import render

def index(request):
    return render(request, 'shared/base.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')