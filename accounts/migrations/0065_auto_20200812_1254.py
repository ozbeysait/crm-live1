# Generated by Django 3.0.6 on 2020-08-12 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0064_auto_20200812_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='emailStatu',
            new_name='emailStatus',
        ),
    ]
