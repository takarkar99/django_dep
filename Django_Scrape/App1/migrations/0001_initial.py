# Generated by Django 5.0.6 on 2024-06-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geonode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, max_length=250, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('protocal', models.CharField(blank=True, max_length=250, null=True)),
                ('country', models.CharField(blank=True, max_length=250, null=True)),
                ('Uptime', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
