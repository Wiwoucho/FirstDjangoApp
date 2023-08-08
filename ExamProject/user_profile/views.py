from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .forms import ProfileEditForm
from ..main.forms import RegistrationForm



class profile_details(views.View):
    template_name = 'profile/profile_details.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        context = {
            'user': user,
        }
        return render(request, self.template_name, context)


class edit_profile_view(LoginRequiredMixin, views.View):
    template_name = 'profile/profile_edit.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = ProfileEditForm(instance=user)  # Use the instance parameter to populate the form
        context = {
            'form': form,
            'user': user,
        }
        return render(request, self.template_name, context)



