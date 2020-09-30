from django.contrib.auth.models import AbstractUser
from django.db import models


class RobowizardEmployee(AbstractUser):
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
