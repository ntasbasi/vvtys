# Generated by Django 2.1.15 on 2020-05-27 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vvtys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoName', models.CharField(db_column='videoName', help_text='Lütfen Video ismini Boş Geçmeyiniz', max_length=200, verbose_name='Video Adı :')),
            ],
        ),
        migrations.RenameField(
            model_name='tablo',
            old_name='isim',
            new_name='videoName',
        ),
    ]