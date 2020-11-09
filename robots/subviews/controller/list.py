from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from robots.models import *


class ControllerListView(LoginRequiredMixin, ListView):
    model = Controller
    template_name = 'robots/controller/list.html'
    login_url = 'login'
