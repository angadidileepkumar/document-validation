from django.shortcuts import render

# Create your views here.
# myapp/views.py

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dash.html')
