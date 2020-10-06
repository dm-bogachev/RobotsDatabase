from django.db import models
from django.utils import timezone
from  django.forms import SelectDateWidget


class Robot(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
    )

    # Текстовое поле из-за ниличия серийных номеров с буквой С
    serial_number = models.CharField(
        max_length=32,
        verbose_name='Серийный номер',
    )

    description = models.TextField(
        verbose_name='Описание',
    )

    shipping_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата поставки', )

    creation_date = models.DateField(
        auto_now=True,
    )

    controller_id = models.ForeignKey(
        'Controller',
        on_delete=models.CASCADE,
        verbose_name='Контроллер',
    )

    model_id = models.ForeignKey(
        'Arm',
        on_delete=models.CASCADE,
        verbose_name='Модель',
    )

    client_id = models.ForeignKey(
        'Client',
        on_delete=models.CASCADE,
        verbose_name='Клиент',
    )

    integrator_id = models.ForeignKey(
        'Integrator',
        on_delete=models.CASCADE,
        verbose_name='Интегратор',
        null=True,
        blank=True,
    )

    # # Временно чарфилд, потом будет файл
    # main_backup = models.CharField(
    #     max_length=512,
    #     verbose_name='Путь к бэкапу',
    #     null=True,
    #     blank=True,
    # )

    main_backup_file = models.FileField(
        verbose_name='Бэкап',
        null=True,
        blank=True,
        upload_to='backups/'
    )

    def __str__(self):
        return self.name


class Arm(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name="Модель",
    )

    def __str__(self):
        return self.name


class Controller(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name="Контроллер",
    )

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Клиент",
        unique=True,
    )

    location_id = models.ForeignKey(
        'Location',
        on_delete=models.DO_NOTHING,
        verbose_name='Местоположение',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


# Интегратор
class Integrator(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Интегратор",
        unique=True,
    )

    location_id = models.ForeignKey(
        'Location',
        on_delete=models.DO_NOTHING,
        verbose_name='Местоположение',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.CharField(
        max_length=255,
        verbose_name='Страна',
    )

    city = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Город',
    )

    def __str__(self):
        return self.country + "/" + self.city


class Backup(models.Model):
    file = models.FileField(
        verbose_name='Файл',
        upload_to='backups/',
        # # Временно, пока не обеспечу загрузку файлов
        # blank=True,
        # null=True,
    )
    # file_path = models.CharField(
    #     max_length=1024,
    #     verbose_name='Путь к файлу'
    # )
    service_id = models.ForeignKey(
        'Service',
        on_delete=models.DO_NOTHING
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        null=True,
        blank=True,
    )

    def __str__(self):
        return "Backup" + str(self.id)


class Service(models.Model):
    date = models.DateField(
        verbose_name='Дата',
    )
    report = models.FileField(
        null=True,
        blank=True,
        upload_to='reports/',
        verbose_name='Отчёт',
    )
    # report_path = models.CharField(
    #     max_length=512,
    #     null=True,
    #     blank=True,
    #     verbose_name='Путь к файлу'
    # )
    description = models.TextField(
        verbose_name='Описание',
    )

    robot_id = models.ForeignKey(
        'Robot',
        on_delete=models.CASCADE,
        verbose_name='Робот',
    )

    def __str__(self):
        return self.description

    @property
    def days_from_service(self):
        from datetime import datetime
        date_format = "%d.%m.%Y"
        a = datetime.strptime(str(datetime.now().date()), date_format)
        b = datetime.strptime(str(self.date), date_format)
        delta = b - a
        if delta < 0:
            return str(-delta.days) + ' дней назад'
        else:
            return 'Запланировано на ' + self.date + ' (через ' + -delta.days + ' дней'

