# Generated by Django 4.2.9 on 2024-01-14 17:25

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
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('serial', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alarmavecinal.country')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('police', models.CharField(max_length=14)),
                ('fireemergency', models.CharField(max_length=14)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('device', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='alarmavecinal.device')),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256)),
                ('address2', models.CharField(max_length=256)),
                ('street_number', models.CharField(max_length=256)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alarmavecinal.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alarmavecinal.country')),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alarmavecinal.neighborhood')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alarmavecinal.state')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=256)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('delivered', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alarmavecinal.state'),
        ),
    ]
