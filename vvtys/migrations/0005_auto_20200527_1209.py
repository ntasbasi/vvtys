# Generated by Django 2.1.15 on 2020-05-27 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vvtys', '0004_auto_20200527_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='oTarihi',
            field=models.DateTimeField(blank=True, db_column='oTarihi', default=datetime.datetime(2020, 5, 27, 12, 9, 46, 386486), verbose_name='Oluşturulma tarihi'),
        ),
    ]
