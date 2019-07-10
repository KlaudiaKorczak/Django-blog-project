from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Paintings, Question, Comment
from .forms import CommentForm
from .utils.results import Results

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def paintings(request, message = None):
    paintings_data = Paintings.objects
    current_comments = Comment.objects
    # if request.method == 'POST':
    #     comment_form = CommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         comment_form.save()
    # else:
    comment_form = CommentForm()
    return render(request, 'paintings.html', {'paintings_data': paintings_data,
                                              'current_comments': current_comments,
                                              'comment_form': comment_form})


def comments(request):
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.save()
        return HttpResponseRedirect(reverse('paintings'))

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
