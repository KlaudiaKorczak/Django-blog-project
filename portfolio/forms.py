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
