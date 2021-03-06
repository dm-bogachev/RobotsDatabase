# Generated by Django 3.1.1 on 2020-09-30 20:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0003_auto_20200930_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robowizardemployee',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='robowizardemployee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='robowizardemployee',
            name='mid_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='robowizardemployee',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность'),
        ),
    ]
