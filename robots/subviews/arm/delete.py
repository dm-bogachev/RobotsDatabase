from django.views.generic import DeleteView
from robots.models import Arm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ArmDeleteView(LoginRequiredMixin, DeleteView):
    model = Arm
    template_name = 'robots/arm/delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')

