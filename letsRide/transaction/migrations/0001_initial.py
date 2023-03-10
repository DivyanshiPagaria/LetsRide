# Generated by Django 3.0.5 on 2022-12-16 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='rider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_from', models.CharField(max_length=20)),
                ('location_to', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('travel_medium', models.CharField(choices=[('BUS', 'bus'), ('CAR', 'car'), ('TRN', 'train')], max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='requester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_from', models.CharField(max_length=20)),
                ('location_to', models.CharField(max_length=20)),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('asset_type', models.CharField(choices=[('BAG', 'travel_bag'), ('PKG', 'package'), ('LPT', 'laptop')], max_length=3)),
                ('asset_sensitivity', models.CharField(choices=[('HIGH', 'highly_sensitive'), ('NRML', 'sensitive'), ('LOW', 'normal')], max_length=4)),
                ('receiver', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
