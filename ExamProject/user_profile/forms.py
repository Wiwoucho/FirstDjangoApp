from django import forms
from django.contrib.auth import forms as auth_forms


class ProfileEditForm(auth_forms.UserCreationForm):

    email = forms.EmailField(
        max_length = 100,
    )

    image = forms.ImageField(
        required = False
    )

    class Meta(auth_forms.UserCreationForm.Meta):
        fields = auth_forms.UserCreationForm.Meta.fields + ('email', 'image')

