import os
from django.views.generic import *
from database import settings
from robots.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ControllerCreateView(LoginRequiredMixin, CreateView):
    model = Controller
    template_name = 'robots/controller/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')

