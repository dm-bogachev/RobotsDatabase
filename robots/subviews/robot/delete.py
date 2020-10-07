from django.views.generic import DeleteView
from robots.models import Robot
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class RobotDeleteView(LoginRequiredMixin, DeleteView):
    model = Robot
    template_name = 'robots/robot/delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')

