from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book

    
class ReviewForm(forms.Form):
    rating = forms.IntegerField(label="Avaliação", min_value=1, max_value=5)
    comment = forms.Charfield(label= "Seu comentário sobre o livro", widget=forms.Textarea(attrs={'rows': 4}))

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date')