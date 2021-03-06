# Generated by Django 2.1.15 on 2020-06-10 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vvtys', '0011_att'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('att', models.TextField(db_column='att', default='', max_length=500, verbose_name='Anahtar Değerler :')),
                ('baslangicSure', models.TextField(db_column='baslangicSure', default='', max_length=500, verbose_name='Süre Değerler :')),
                ('bitisSure', models.TextField(db_column='bitisSure', default='', max_length=500, verbose_name='Süre Değerler :')),
                ('attTypeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vvtys.AttType')),
                ('videoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vvtys.Video')),
            ],
        ),
    ]
