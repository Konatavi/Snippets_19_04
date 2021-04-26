from django.forms import ModelForm
from MainApp.models import Snippet
from django import forms


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        widgets = {
            'name': forms.TextInput(attrs={'class': 'red'})
        }
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code']
