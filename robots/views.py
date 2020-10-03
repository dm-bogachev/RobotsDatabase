from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from django.http import request
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(LoginRequiredMixin, ListView):
    model = Robot
    template_name = 'robots/home.html'
    login_url = 'login'


class ArmCreateView(LoginRequiredMixin, CreateView):
    model = Arm
    template_name = 'robots/arm/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')


class BackupCreateView(LoginRequiredMixin, CreateView):
    model = Backup
    template_name = 'robots/backup/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'robots/client/create.html'
    fields = '__all__'
    login_url = 'login'

    @staticmethod
    def all_locations():
        return Location.objects.all()

    def get_success_url(self):
        return reverse_lazy('home')


class ControllerCreateView(LoginRequiredMixin, CreateView):
    model = Controller
    template_name = 'robots/controller/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')


class IntegratorCreateView(LoginRequiredMixin, CreateView):
    model = Integrator
    template_name = 'robots/client/create.html'
    fields = '__all__'
    login_url = 'login'

    @staticmethod
    def all_locations():
        return Location.objects.all()

    def get_success_url(self):
        return reverse_lazy('home')


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    template_name = 'robots/location/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')


class RobotCreateView(LoginRequiredMixin, CreateView):
    model = Robot
    template_name = 'robots/robot/create.html'
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


class RobotUpdateView(LoginRequiredMixin, UpdateView):
    model = Robot
    template_name = 'robots/robot/update.html'
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
        return reverse_lazy('robot_read', kwargs={'pk': self.kwargs['pk']})


class RobotDeleteView(LoginRequiredMixin, DeleteView):
    model = Robot
    template_name = 'robots/robot/delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = 'robots/service/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')
