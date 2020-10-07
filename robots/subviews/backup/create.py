import os
from django.views.generic import *
from database import settings
from robots.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class BackupCreateView(LoginRequiredMixin, CreateView):
    model = Backup
    template_name = 'robots/backup/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        return super(BackupCreateView, self).form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        self.file = request.FILES.pop('file', None)
        if isinstance(self.file, list) and len(self.file) > 0:
            self.file = self.file[0]
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        if self.file:
            upload_to = form.instance.file.field.upload_to
            save_folder = settings.MEDIA_ROOT + upload_to
            filename, file_extension = os.path.splitext(self.file.name)
            new_filename = upload_to.replace('s/', '_') + str(len(os.listdir(save_folder))).zfill(3) + file_extension
            with open((save_folder + new_filename), 'wb+') as f:
                for chunk in self.file.chunks():
                    f.write(chunk)
            form.instance.file = upload_to + new_filename
        form.save()
        return super(BackupCreateView, self).form_valid(form)

