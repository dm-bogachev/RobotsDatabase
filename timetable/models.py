from django.db import models
from users.models import RobowizardEmployee


class WorkingPlace(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self):
        return self.name


class WorkingDay(models.Model):
    date = models.DateField(verbose_name='Дата')
    employee = models.ForeignKey(RobowizardEmployee, on_delete=models.DO_NOTHING, verbose_name='Работник')

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

    def get_workingdayparts(self):
        return WorkingDayPart.objects.filter(workingday_id=self.id)

    @property
    def get_number_of_workingdayparts(self):
        return WorkingDayPart.objects.filter(workingday_id_id=self.id)

    @property
    def get_maxworkingdaypartsnumber(self):
        max = 0
        for obj in WorkingDayPart.objects.filter(workingday_id_id=self.id):
            if len(obj) > max:
                max = len(obj)
        return  max

    # def all_workingdayparts(self):
    #     return WorkingDayPart.objects.all()


class WorkingDayPart(models.Model):
    workingday_id = models.ForeignKey(WorkingDay, on_delete=models.DO_NOTHING, verbose_name='Дата')
    begin_time = models.TimeField(verbose_name='Начало')
    end_time = models.TimeField(verbose_name='Конец')
    location_id = models.ForeignKey(WorkingPlace, verbose_name='Место', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.begin_time.strftime('%H:%M') + "-" + self.end_time.strftime('%H:%M')
