from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import DeleteView

from robots.models import Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'robots/client/delete.html'
    login_url = 'login'

    # def get_success_url(self):
    #     return reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        return HttpResponse('<script>opener.closeDeletePopup(window);</script>')
