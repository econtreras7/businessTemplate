import re
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
# Replace the existing home function with the one below
def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")
# You can also remove the import re statement that's no longer used

def hello_there(request, name):
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )