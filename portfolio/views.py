from django.shortcuts import render

from .models import Paintings, Question
from .utils.results import Results

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def paintings(request):
    paintings_data = Paintings.objects
    return render(request, 'paintings.html', {'paintings_data': paintings_data})


def polling(request):
    questions = Question.objects
    return render(request, 'polling.html', {'questions': questions})


def results(request):
    questions = Question.objects

    q_data = request.POST.dict()
    statistics = Results.get_results(q_data)

    return render(request, 'results.html', {'statistics': statistics, 'questions': questions})


def contact(request):
    return render(request, 'contact.html')
