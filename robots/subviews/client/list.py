from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from robots.models import *


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'robots/client/list.html'
    login_url = 'login'
