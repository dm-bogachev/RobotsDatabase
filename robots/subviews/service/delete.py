from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from robots.models import Service, Robot


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    template_name = 'robots/service/delete.html'
    login_url = 'login'

    def get_success_url(self):
        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(service=pk)
        return reverse_lazy('robot_read', kwargs={'pk': robot.pk})
        # return reverse_lazy('home')
