from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from robots.models import *


class ArmListView(LoginRequiredMixin, ListView):
    model = Arm
    template_name = 'robots/arm/list.html'
    login_url = 'login'
