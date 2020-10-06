import os

from django.core.files.storage import default_storage
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from django.http import request
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings


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

    def form_invalid(self, form):
        return super(RobotCreateView, self).form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        self.main_backup_file = request.FILES.pop('main_backup_file', None)
        if isinstance(self.main_backup_file, list) and len(self.main_backup_file) > 0:
            self.main_backup_file = self.main_backup_file[0]
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        upload_to = form.instance.main_backup_file.field.upload_to
        save_folder = settings.MEDIA_ROOT + upload_to
        new_filename = upload_to.replace('s/', '_') + str(len(os.listdir(save_folder))).zfill(3)
        if self.main_backup_file:
            with open((save_folder + new_filename), 'wb+') as f:
                for chunk in self.main_backup_file.chunks():
                    f.write(chunk)
        #
        form.instance.main_backup_file = upload_to + new_filename
        form.save()
        return super(RobotCreateView, self).form_valid(form)


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
