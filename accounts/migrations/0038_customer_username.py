# Generated by Django 3.0.6 on 2020-07-28 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20200727_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='userName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.User'),
        ),
    ]
