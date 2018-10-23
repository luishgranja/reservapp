from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'documento', 'email', 'password1', 'password2', 'tipo',
                  'is_active')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2', 'is_active']:
            self.fields[fieldname].help_text = None


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'documento', 'username', 'email')


class EditFullProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'documento', 'username', 'email', 'tipo', 'is_active')
