import os
from django.views.generic import *
from robots.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ArmCreateView(LoginRequiredMixin, CreateView):
    model = Arm
    template_name = 'robots/arm/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')

