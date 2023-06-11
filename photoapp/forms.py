from.models import Photoblog
from django import forms

class BlogForm(forms.ModelForm):

    class Meta:


        model = Photoblog

        fields = ['image', 'title', 'author', 'text']