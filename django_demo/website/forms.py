from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book

class LogUsers(UserCreationForm):
     
     class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome de Usuário'
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>* Obrigatório.</small></span>'

        for field_name in ['password1', 'password2']:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Senha' if field_name == 'password1' else 'Confirme a sua Senha'
            })
            self.fields[field_name].label = ''
            self.fields[field_name].help_text = '<ul class="form-text text-muted small"><li>Sua senha deve conter ao menos 8 caractéres.</li></ul>'


class ReviewForm(forms.Form):
    rating = forms.IntegerField(label="Avaliação", min_value=1, max_value=5)
    comment = forms.Charfield(label= "Seu comentário sobre o livro", widget=forms.Textarea(attrs={'rows': 4}))

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date')