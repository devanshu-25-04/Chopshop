# Generated by Django 4.1.7 on 2023-04-06 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_employee_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
