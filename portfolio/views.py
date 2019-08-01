from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Paintings, Question, Comment
from .forms import CommentForm, ContactForm
from .utils.results import Results


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def paintings(request):
    paintings_data = Paintings.objects
    current_comments = Comment.objects
    if request.method == 'GET':
        comment_form = CommentForm()
    else:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # create but don't save -> assign current post to the comment -> save comment to db
            # new_comment = comment_form.save(commit=False)
            # new_comment.post = post
            comment_form.save()
            return HttpResponseRedirect(reverse(paintings))
    return render(request, 'paintings.html', {'paintings_data': paintings_data,
                                              'current_comments': current_comments,
                                              'comment_form': comment_form})


def polling(request):
    questions = Question.objects
    return render(request, 'polling.html', {'questions': questions})


def results(request):
    questions = Question.objects

    q_data = request.POST.dict()
    statistics = Results.get_results(q_data)

    return render(request, 'results.html', {'statistics': statistics, 'questions': questions})


def contact(request):
    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            email_from = contact_form.cleaned_data['email_from']
            name = contact_form.cleaned_data['name']
            subject = 'Blog contact: message from user %s' % name
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, email_from, ['klaudiakor95@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact.html', {'contact_form': contact_form})


def success(request):
    message = 'Thank You for Your message!'
    return render(request, 'success.html', {'message': message})
