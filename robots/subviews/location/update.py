from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import UpdateView

from robots.models import *


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    model = Location
    template_name = 'robots/location/update.html'
    fields = '__all__'
    login_url = 'login'

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_client");</script>' % (instance.pk, instance))
