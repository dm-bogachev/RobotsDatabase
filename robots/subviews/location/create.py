from django.views.generic import *
from robots.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    template_name = 'robots/location/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')
