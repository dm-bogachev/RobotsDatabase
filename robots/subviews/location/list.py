from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from robots.models import *


class LocationListView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'robots/location/list.html'
    login_url = 'login'
