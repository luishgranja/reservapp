# Generated by Django 2.0.1 on 2018-11-07 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(choices=[('Computador', 'Computador de Mesa'), ('video', 'Video Beam'), ('Bafle', 'Bafle'), ('Portatil', 'Portatil'), ('cable-vga', 'Cable VGA'), ('cable-poder', 'Cable poder'), ('cable-hdmi', 'Cable HDMI')], default='Computador', max_length=15)),
                ('is_active', models.BooleanField(default=True)),
                ('condicion', models.CharField(choices=[('Pesimo', 'Pésimo (1)'), ('Malo', 'Malo (2)'), ('Regular', 'Regular (3)'), ('Bueno', 'Bueno (4)'), ('Excelente', 'Excelente (5)')], default='Excelente', max_length=11)),
                ('observaciones', models.TextField(max_length=150)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
    ]
