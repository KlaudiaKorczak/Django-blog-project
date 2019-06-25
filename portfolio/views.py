from django.shortcuts import render
from .models import Paintings
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def paintings(request):
    paintings_data = Paintings.objects
    return render(request, 'paintings.html', {'paintings_data': paintings_data})


def questionnaire(request):
    return render(request, 'questionnaire.html')
