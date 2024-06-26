# Generated by Django 4.1.1 on 2022-10-31 20:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('Filler', 'Filler'), ('Botox', 'Botox'), ('Nakh', 'Nakh'), ('Javansazi', 'Javansazi'), ('Laghari', 'Laghari'), ('Lazer', 'Lazer'), ('Bardasht Ghabghab', 'Bardasht Ghabghab'), ('Bardasht Khal', 'Bardasht Khal'), ('Subsision', 'Subsision'), ('Termia', 'Termia'), ('Tarmim', 'Tarmim'), ('Moshavere', 'Moshavere'), ('Other', 'Other')], default='Other', max_length=50)),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('3 PM', '3 PM'), ('3:30 PM', '3:30 PM'), ('4 PM', '4 PM'), ('4:30 PM', '4:30 PM'), ('5 PM', '5 PM'), ('5:30 PM', '5:30 PM'), ('6 PM', '6 PM'), ('6:30 PM', '6:30 PM'), ('7 PM', '7 PM'), ('7:30 PM', '7:30 PM')], default='3 PM', max_length=10)),
                ('time_ordered', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]