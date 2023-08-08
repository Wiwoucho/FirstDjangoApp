from django.urls import path
from .views import profile_details, edit_profile_view

urlpatterns = [
    path('profile_details/<int:pk>', profile_details.as_view(), name='profile_details'),
    path('edit_profile/<int:pk>', edit_profile_view.as_view(), name='edit_profile')
]