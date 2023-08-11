from django import forms
from django.contrib.auth import forms as auth_forms


class ProfileEditForm(auth_forms.UserCreationForm):

    email = forms.EmailField(
        max_length = 100,
    )

    username = forms.CharField(max_length = 30)
    class Meta(auth_forms.UserCreationForm.Meta):
        fields = auth_forms.UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['password1'].help_text = False
        self.fields['password2'].help_text = False

    def update_user(self, user_instance):
        user_instance.username = self.cleaned_data['username']
        user_instance.email = self.cleaned_data['email']
        user_instance.first_name = self.cleaned_data['first_name']
        user_instance.last_name = self.cleaned_data['last_name']
        user_instance.save()


