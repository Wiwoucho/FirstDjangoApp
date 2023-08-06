from django.urls import path
from .views import profile_details

urlpatterns = [
    path('profile_details/<int:pk>', profile_details.as_view(), name='profile_details')
]