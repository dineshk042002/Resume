from django.shortcuts import render
from .models import Resume

def home(request):
    resume = Resume.objects.first()
    return render(request, 'Dinesh/home.html', {'resume': resume})
