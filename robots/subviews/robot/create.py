import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from robots.models import *


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

        if self.main_backup_file:
            upload_to = form.instance.main_backup_file.field.upload_to
            save_folder = settings.MEDIA_ROOT + upload_to
            filename, file_extension = os.path.splitext(self.main_backup_file.name)
            new_filename = upload_to.replace('s/', '_') + str(len(os.listdir(save_folder))).zfill(3) + file_extension
            with open((save_folder + new_filename), 'wb+') as f:
                for chunk in self.main_backup_file.chunks():
                    f.write(chunk)
            form.instance.main_backup_file = upload_to + new_filename

        form.save()
        return super(RobotCreateView, self).form_valid(form)
