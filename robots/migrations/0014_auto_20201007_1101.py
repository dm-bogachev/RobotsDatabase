# Generated by Django 3.1.2 on 2020-10-07 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0013_auto_20201006_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='controller_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='robots.controller', verbose_name='Контроллер'),
        ),
    ]