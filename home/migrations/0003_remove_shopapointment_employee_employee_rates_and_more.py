# Generated by Django 4.1.7 on 2023-04-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_shopapointment_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopapointment',
            name='employee',
        ),
        migrations.AddField(
            model_name='employee',
            name='rates',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='shopapointment',
            name='name1',
            field=models.CharField(default='', max_length=20),
        ),
    ]
