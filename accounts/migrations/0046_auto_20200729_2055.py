# Generated by Django 3.0.6 on 2020-07-29 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_auto_20200729_2013'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactFormMessage',
            new_name='Tickets',
        ),
    ]
