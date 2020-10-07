from django.views.generic import DeleteView
from robots.models import Location
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LocationDeleteView(LoginRequiredMixin, DeleteView):
    model = Location
    template_name = 'robots/location/delete.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')

