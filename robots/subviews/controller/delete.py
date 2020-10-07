from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from robots.models import Controller


class ControllerDeleteView(LoginRequiredMixin, DeleteView):
    model = Controller
    template_name = 'robots/controller/delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')
