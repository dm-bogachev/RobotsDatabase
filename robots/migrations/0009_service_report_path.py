# Generated by Django 3.1.1 on 2020-10-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('robots', '0008_auto_20201002_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='report_path',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Путь к файлу'),
        ),
    ]
