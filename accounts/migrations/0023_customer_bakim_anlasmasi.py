# Generated by Django 3.0.6 on 2020-05-18 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20200518_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bakim_anlasmasi',
            field=models.CharField(choices=[('Aktif', 'Aktif'), ('Pasif', 'Pasif')], max_length=200, null=True),
        ),
    ]
