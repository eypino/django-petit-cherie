from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

GENDER_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
]

class CustomUserCreationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    phone_number = PhoneNumberField(label='Número de teléfono', region='CL', required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Género', required=True)
    address = forms.CharField(max_length=100, label='Dirección', required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'gender', 'address', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso')
        return username
