from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import UpdateView

from robots.models import *


class ControllerUpdateView(LoginRequiredMixin, UpdateView):
    model = Controller
    template_name = 'robots/controller/update.html'
    fields = '__all__'
    login_url = 'login'

    def form_valid(self, form):
        instance = form.save()
        return HttpResponse(
            '<script>opener.closePopup(window, "%s", "%s", "#id_client");</script>' % (instance.pk, instance))
