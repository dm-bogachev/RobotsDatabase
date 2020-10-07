from django.views.generic import DetailView
from robots.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class RobotReadView(LoginRequiredMixin, DetailView):
    template_name = 'robots/robot/read.html'
    model = Robot
    fields = '__all__'
    login_url = 'login'

    @staticmethod
    def all_clients():
        return Client.objects.all()

    @staticmethod
    def all_arms():
        return Arm.objects.all()

    @staticmethod
    def all_controllers():
        return Controller.objects.all()

    @staticmethod
    def all_integrator():
        return Integrator.objects.all()

    def get_success_url(self):
        return reverse_lazy('home')

