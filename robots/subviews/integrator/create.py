import os
from django.views.generic import *
from database import settings
from robots.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class IntegratorCreateView(LoginRequiredMixin, CreateView):
    model = Integrator
    template_name = 'robots/client/create.html'
    fields = '__all__'
    login_url = 'login'

    @staticmethod
    def all_locations():
        return Location.objects.all()

    def get_success_url(self):
        return reverse_lazy('home')

