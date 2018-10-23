# Generated by Django 2.0.1 on 2018-10-23 05:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recursos', '0002_auto_20181022_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='usuarios',
            field=models.ManyToManyField(through='reservas.Reserva', to=settings.AUTH_USER_MODEL),
        ),
    ]