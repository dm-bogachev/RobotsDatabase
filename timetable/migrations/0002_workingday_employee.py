# Generated by Django 3.1.2 on 2020-11-13 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workingday',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Работник'),
        ),
    ]