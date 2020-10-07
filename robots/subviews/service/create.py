import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *

from robots.models import *


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = 'robots/service/create.html'
    fields = ['date', 'report', 'description']
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('robot_read', kwargs={'pk': self.kwargs['pk']})

    def form_invalid(self, form):
        return super(ServiceCreateView, self).form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        self.report = request.FILES.pop('report', None)
        if isinstance(self.report, list) and len(self.report) > 0:
            self.report = self.report[0]
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        if self.report:
            upload_to = form.instance.report.field.upload_to
            save_folder = settings.MEDIA_ROOT + upload_to
            filename, file_extension = os.path.splitext(self.report.name)
            new_filename = upload_to.replace('s/', '_') + str(len(os.listdir(save_folder))).zfill(3) + file_extension
            with open((save_folder + new_filename), 'wb+') as f:
                for chunk in self.report.chunks():
                    f.write(chunk)
            form.instance.report = upload_to + new_filename

        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(pk=pk)
        form.instance.robot_id = robot
        form.save()
        return super(ServiceCreateView, self).form_valid(form)
