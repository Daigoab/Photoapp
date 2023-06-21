from.models import Photoblog, Comment
from django import forms

class BlogForm(forms.ModelForm):

    class Meta:


        model = Photoblog

        fields = ['image', 'title', 'author', 'text']

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '4',
    }))
    class Meta:
        model = Comment
        fields = ['text']