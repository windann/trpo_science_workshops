# Generated by Django 2.2.7 on 2019-11-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops_app', '0003_auto_20191127_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='scienceworkshop',
            name='left_places',
            field=models.IntegerField(null=True, verbose_name='Осталось мест'),
        ),
    ]
