from django import forms


def guests_validator(value):
    if value < 1:
        raise forms.ValidationError("Number of guests must be greater than or equal to 1.")