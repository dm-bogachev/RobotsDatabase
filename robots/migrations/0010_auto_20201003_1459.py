# Generated by Django 3.1.2 on 2020-10-03 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0009_service_report_path'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='robot',
            options={'verbose_name': 'Робот', 'verbose_name_plural': 'Роботов'},
        ),
    ]
