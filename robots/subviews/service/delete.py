from django.views.generic import DeleteView
from robots.models import Service
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    template_name = 'robots/service/delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')

