from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, post_delete

from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler


class RobowizardEmployee(ChangeloggableMixin, AbstractUser):
    username = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Имя пользователя', )

    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        verbose_name='E-Mail',
    )

    first_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Имя', )

    last_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Фамилия', )

    mid_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Отчество', )

    position = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Должность',
    )

    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
    )

    permission_service = models.BooleanField(verbose_name='Сервисный отдел', default=False)
    permission_sales = models.BooleanField(verbose_name='Отдел продаж', default=False)
    permission_accounting = models.BooleanField(verbose_name='Бухгалтерия', default=False)
    permission_administration = models.BooleanField(verbose_name='Администратор', default=False)

    def save(self, *args, **kwargs):
        self.is_superuser = self.permission_administration
        self.is_staff = self.permission_administration
        super(RobowizardEmployee, self).save(*args, **kwargs)


post_save.connect(journal_save_handler, sender=RobowizardEmployee)
post_delete.connect(journal_delete_handler, sender=RobowizardEmployee)
