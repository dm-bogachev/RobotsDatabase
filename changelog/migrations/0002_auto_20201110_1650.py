# Generated by Django 3.1.2 on 2020-11-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('changelog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changelog',
            name='data',
            field=models.TextField(),
        ),
    ]
