# Generated by Django 2.1.7 on 2019-03-19 03:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='S_Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
