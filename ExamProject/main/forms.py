from django import forms
from django.contrib.auth.models import User
from .models import AddBookingModel, LoginModel
from django.contrib.auth import forms as auth_forms
from django.core.validators import MinLengthValidator


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
        self.fields['username'].validators = [MinLengthValidator(5, 'username should be at least 5 symbols.')]

    def clean_username(self):
        username = self.cleaned_data['username'].lower()  # Convert username to lowercase
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError("Username already exists!")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("Email already exists!")
        return email


class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput,
        }



