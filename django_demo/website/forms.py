from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Reader


class Register(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', ' password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nome de Usuário'
        })
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><smal>* Obrigatório.</small></span>'

        for field_name in ['password1', 'password2']:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Senha' if field_name == 'password1' else 'Confirme a sua Senha'
            })
            self.fields[field_name].label = ''
            self.fields[field_name].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser muito semelhante a suas outras informações pessoais.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li></ul'