from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Paintings, Question, Choice
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


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    result1 = {"cos1":"cos1", "cos2": "cos2"}
    context = {"result": result1, "q": question}
    return render(request, 'results.html', context)


def vote(request):

    return HttpResponse(request)
        # return HttpResponseRedirect(reverse('results', args=(question.id,)))


def contact(request):
    return render(request, 'contact.html')
