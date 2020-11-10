from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from robots.models import *


class IntegratorListView(LoginRequiredMixin, ListView):
    model = Integrator
    template_name = 'robots/integrator/list.html'
    login_url = 'login'
