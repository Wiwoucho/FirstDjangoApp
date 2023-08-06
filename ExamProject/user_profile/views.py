from django.shortcuts import render
from django.views import generic as views
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



class profile_details(views.View):
    template_name = 'profile/profile_details.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        context = {
            'user': user,
        }
        return render(request, self.template_name, context)