# Generated by Django 3.0.6 on 2020-05-18 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20200518_0510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='pruduct_key',
            new_name='product_key',
        ),
    ]
