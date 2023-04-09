# Generated by Django 4.1.7 on 2023-04-05 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_shopapointment_employee_employee_rates_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopapointment',
            name='name1',
        ),
        migrations.AddField(
            model_name='shopapointment',
            name='employee',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
