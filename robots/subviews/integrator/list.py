from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from robots.models import *


class IntegratorListView(LoginRequiredMixin, ListView):
    model = Integrator
    template_name = 'robots/integrator/list.html'
    login_url = 'login'
