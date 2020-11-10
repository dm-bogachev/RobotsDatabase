from django.db import models
from django.db.models.signals import post_delete, post_save

from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler


class Robot(ChangeloggableMixin, models.Model):
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
        blank=True,
        null=True,
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
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Контроллер',
    )

    model_id = models.ForeignKey(
        'Arm',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Модель',
    )

    client_id = models.ForeignKey(
        'Client',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Клиент',
    )

    integrator_id = models.ForeignKey(
        'Integrator',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Интегратор',
        blank=True,
    )

    main_backup_file = models.FileField(
        verbose_name='Бэкап',
        null=True,
        blank=True,
        upload_to='backups/'
    )

    def __str__(self):
        return self.name


class Arm(ChangeloggableMixin, models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name="Модель",
    )

    def __str__(self):
        return self.name


class Controller(ChangeloggableMixin, models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
        verbose_name="Контроллер",
    )

    def __str__(self):
        return self.name


class Client(ChangeloggableMixin, models.Model):
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
class Integrator(ChangeloggableMixin, models.Model):
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


class Location(ChangeloggableMixin, models.Model):
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


class Backup(ChangeloggableMixin, models.Model):
    file = models.FileField(
        verbose_name='Файл',
        upload_to='backups/',
        # # Временно, пока не обеспечу загрузку файлов
        # blank=True,
        # null=True,
    )

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


class Service(ChangeloggableMixin, models.Model):
    date = models.DateField(
        verbose_name='Дата',
    )
    report = models.FileField(
        null=True,
        blank=True,
        upload_to='reports/',
        verbose_name='Отчёт',
    )

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
        date_format = "%Y-%m-%d"
        a = datetime.strptime(str(datetime.now().date()), date_format)
        b = datetime.strptime(str(self.date), date_format)
        delta = b - a
        if delta.days < 0:
            return str(-delta.days) + ' дней назад'
        else:
            return 'Запланировано на ' + str(self.date.strftime("%d.%m.%Y")) + ' (через ' + str(
                delta.days) + ' дня(ей))'


post_save.connect(journal_save_handler, sender=Robot)
post_delete.connect(journal_delete_handler, sender=Robot)

#
post_save.connect(journal_save_handler, sender=Arm)
post_delete.connect(journal_delete_handler, sender=Arm)
#
post_save.connect(journal_save_handler, sender=Backup)
post_delete.connect(journal_delete_handler, sender=Backup)
#
post_save.connect(journal_save_handler, sender=Client)
post_delete.connect(journal_delete_handler, sender=Client)
#
post_save.connect(journal_save_handler, sender=Controller)
post_delete.connect(journal_delete_handler, sender=Controller)
#
post_save.connect(journal_save_handler, sender=Integrator)
post_delete.connect(journal_delete_handler, sender=Integrator)
#
post_save.connect(journal_save_handler, sender=Location)
post_delete.connect(journal_delete_handler, sender=Location)
#
post_save.connect(journal_save_handler, sender=Service)
post_delete.connect(journal_delete_handler, sender=Service)
