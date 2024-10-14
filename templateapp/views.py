from django.shortcuts import render

def home(request):
    return render(request,"templateapp/home.html")

def about(request):
    return render(request,"templateapp/about.html")

def furniture(request):
    return render(request,"templateapp/furniture.html")

def blog(request):
    return render(request,"templateapp/blog.html")

def contact(request):
    return render(request,"templateapp/contact.html")