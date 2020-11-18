from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from .models import *
from django.template.defaulttags import register


class StaffListView(LoginRequiredMixin, ListView):
    model = WorkingDay
    template_name = 'timetable/staff_list.html'
    login_url = 'login'

    @staticmethod
    def all_workingdayparts():
        return WorkingDayPart.objects.all()

    @staticmethod
    def all_workingplaces():
        return WorkingPlace.objects.all()


class StaffDetailView(LoginRequiredMixin, DetailView):
    model = WorkingDay

