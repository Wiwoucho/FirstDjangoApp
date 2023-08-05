from django.urls import path
from ..main.views import AddBookingView, LoginView, RegistrationView, MyLogoutoView, AboutUsView

urlpatterns = [
    path('AddBooking/', AddBookingView.as_view(), name='AddBooking'),
    path('login/', LoginView.as_view(), name='Login'),
    path('registration/', RegistrationView.as_view(), name='Registration'),
    path('logout/', MyLogoutoView.as_view(), name='Logout'),
    path('aboutus/', AboutUsView.as_view(), name='AboutUs')
]