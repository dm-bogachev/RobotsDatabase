from .subviews import *


class HomePageView(LoginRequiredMixin, ListView):
    model = Robot
    template_name = 'robots/home.html'
    login_url = 'login'
