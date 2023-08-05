from django.shortcuts import render, redirect

from .forms import TripBookingForm


def homepage(request):
    if request.method == 'POST':
        form = TripBookingForm(request.POST)
        if form.is_valid():
            return redirect('booking_success')  # Redirect to a success page after successful form submission
    else:
        form = TripBookingForm()

    return render(request, 'home.html', {'form': form})
