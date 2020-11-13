# Generated by Django 3.1.2 on 2020-11-13 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingDayPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_time', models.TimeField(verbose_name='Начало')),
                ('end_time', models.TimeField(verbose_name='Конец')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='timetable.workingplaces', verbose_name='Место')),
                ('workingday_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='timetable.workingday', verbose_name='Дата')),
            ],
        ),
    ]
