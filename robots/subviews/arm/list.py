from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from robots.models import *


class ArmListView(LoginRequiredMixin, ListView):
    model = Arm
    template_name = 'robots/arm/list.html'
    login_url = 'login'
