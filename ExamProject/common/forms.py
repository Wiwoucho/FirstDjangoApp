from django import forms
from .models import TripBooking

class TripBookingForm(forms.ModelForm):
    class Meta:
        model = TripBooking
        fields = ['city', 'guests', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
