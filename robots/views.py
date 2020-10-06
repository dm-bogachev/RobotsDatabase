from .subviews.robot.imports import *


class HomePageView(LoginRequiredMixin, ListView):
    model = Robot
    template_name = 'robots/home.html'
    login_url = 'login'


class ArmCreateView(LoginRequiredMixin, CreateView):
    model = Arm
    template_name = 'robots/arm/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')


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
            new_filename = upload_to.replace('s/', '_') + str(len(os.listdir(save_folder))).zfill(3)
            with open((save_folder + new_filename + file_extension), 'wb+') as f:
                for chunk in self.file.chunks():
                    f.write(chunk)
            form.instance.file = upload_to + new_filename
        form.save()
        return super(BackupCreateView, self).form_valid(form)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'robots/client/create.html'
    fields = '__all__'
    login_url = 'login'

    @staticmethod
    def all_locations():
        return Location.objects.all()

    def get_success_url(self):
        return reverse_lazy('home')


class ControllerCreateView(LoginRequiredMixin, CreateView):
    model = Controller
    template_name = 'robots/controller/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')


class IntegratorCreateView(LoginRequiredMixin, CreateView):
    model = Integrator
    template_name = 'robots/client/create.html'
    fields = '__all__'
    login_url = 'login'

    @staticmethod
    def all_locations():
        return Location.objects.all()

    def get_success_url(self):
        return reverse_lazy('home')


class LocationCreateView(LoginRequiredMixin, CreateView):
    model = Location
    template_name = 'robots/location/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    template_name = 'robots/service/create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('home')

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
            new_filename = upload_to.replace('s/', '_') + str(len(os.listdir(save_folder))).zfill(3)
            with open((save_folder + new_filename + file_extension), 'wb+') as f:
                for chunk in self.report.chunks():
                    f.write(chunk)
            form.instance.report = upload_to + new_filename
        form.save()
        return super(ServiceCreateView, self).form_valid(form)
