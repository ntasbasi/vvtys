# Generated by Django 2.1.15 on 2020-05-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vvtys', '0003_video_otarihi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='oTarihi',
            field=models.DateTimeField(db_column='oTarihi', verbose_name='Oluşturulma tarihi'),
        ),
    ]