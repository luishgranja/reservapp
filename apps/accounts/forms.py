from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','documento', 'username','email','password1', 'password2', 'tipo','is_active')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'documento','username','email')

class EditFullProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','documento', 'username','email', 'tipo','is_active')