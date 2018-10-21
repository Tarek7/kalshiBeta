from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    wallet_number = forms.CharField(help_text='Required. Coinbase wallet eg. 1GVY5eZvtc5bA6EFEGnpqJeHUC5YaV5dsb')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'wallet_number', 'password1', 'password2', )
