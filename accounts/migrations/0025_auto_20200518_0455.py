# Generated by Django 3.0.6 on 2020-05-18 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20200518_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='bakim_baslangic',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='bakim_bitis',
            field=models.DateTimeField(null=True),
        ),
    ]
