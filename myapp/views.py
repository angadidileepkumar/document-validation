from django.shortcuts import render

# Create your views here.
# myapp/views.py

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dash.html')

def submitForm(request):
    return render(request, 'form.html')

def certificate_validation(request):
    return render(request, 'success.html')

def invalid(request):
    return render (request, 'invalid.html')

# views.py
from django.shortcuts import render
from .models import YourModel

def candidate_list(request):
    # Retrieve all objects from the YourModel table
    data = YourModel.objects.all()
    
    # Retrieve objects with specific conditions
    filtered_data = YourModel.objects.filter(candidate_ID='s123')

    # Render the template with the retrieved data
    return render(request, 'data.html', {'data': data})




from django.http import JsonResponse

def candidate_Data(request):
    data = YourModel.objects.all()
    msg = {'msg':'hello from django'}
    return JsonResponse(data)
