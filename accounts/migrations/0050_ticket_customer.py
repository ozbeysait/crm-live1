# Generated by Django 3.0.6 on 2020-07-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_auto_20200729_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='customer',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
