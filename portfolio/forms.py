from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        labels = {'name': 'Your name',
                  'email': 'Your email',
                  'body': 'Message'}
        widgets = {'body': forms.Textarea}


class ContactForm(forms.Form):
    email_from = forms.EmailField(max_length=30, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Your E-mail'}))
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))
