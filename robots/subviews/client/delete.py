from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from robots.models import Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'robots/client/delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')
