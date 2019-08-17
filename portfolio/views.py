from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from blog import settings
from .models import Paintings, Question, Choice, Comment
from .forms import CommentForm, ContactForm
from .utils.data import Data


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
    questions = Question.objects.all()
    statistics = Data.get_results(questions)

    return render(request, 'results.html', {'statistics': statistics, 'questions': questions})


def vote(request):
    q_data = request.POST.dict()
    selected_choices = Data.get_poll_dict(q_data)
    for question_id, choice_id in selected_choices.items():
        question = get_object_or_404(Question, pk=question_id)
        choice = question.choice_set.get(pk=choice_id)
        choice.votes += 1
        choice.save()
    return HttpResponseRedirect(reverse('results'))


def contact(request):
    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            email_from = contact_form.cleaned_data['email_from']
            name = contact_form.cleaned_data['name']
            subject = 'Blog: message from user {} - {}'.format(name, email_from)
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'contact.html', {'contact_form': contact_form})


def success(request):
    message = 'Thank You for Your message!'
    return render(request, 'success.html', {'message': message})
