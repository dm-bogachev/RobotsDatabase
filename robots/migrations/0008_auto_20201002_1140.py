# Generated by Django 3.1.1 on 2020-10-02 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('robots', '0007_auto_20201002_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='service_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='robots.service'),
        ),
    ]
