from django import forms
from .models import AddBookingModel, LoginModel
from django.contrib.auth import forms as auth_forms


class PictureForm(forms.ModelForm):
    class Meta:
        model = AddBookingModel
        fields = ['name', 'price', 'locations', 'guests']


class RegistrationForm(auth_forms.UserCreationForm):
    email = forms.EmailField(
        max_length = 100
    )

    class Meta(auth_forms.UserCreationForm.Meta):
        fields = auth_forms.UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput,
        }



