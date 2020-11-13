from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from changelog.models import ChangeLog


class LogPageView(LoginRequiredMixin, ListView):
    model = ChangeLog
    template_name = 'changelog/home.html'
    login_url = 'login'
