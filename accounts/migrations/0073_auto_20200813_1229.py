# Generated by Django 3.0.6 on 2020-08-13 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0072_auto_20200813_1202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'get_latest_by': 'id'},
        ),
    ]
