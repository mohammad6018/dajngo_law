from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_page(request):
    return render(request, "index.html")

def blog_page(request):
    return render(request, "blog.html")
