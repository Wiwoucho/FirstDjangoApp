from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic as views
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .forms import ProfileEditForm
from ..main.models import AddBookingModel



class profile_details(views.View):
    template_name = 'profile/profile_details.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        properties_info = AddBookingModel.objects.filter(user=user)

        context = {
            'user': user,
            'properties_info': properties_info
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

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = ProfileEditForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.update_user(user)
            return redirect('profile_details', pk=user.pk)
        else:
            context = {
                'form': form,
                'user': user,
            }
            return render(request, self.template_name, context)


