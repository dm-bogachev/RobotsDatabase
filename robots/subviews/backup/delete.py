from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from robots.models import Backup


class BackupDeleteView(LoginRequiredMixin, DeleteView):
    model = Backup
    template_name = 'robots/backup/delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')
