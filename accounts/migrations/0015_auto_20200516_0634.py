# Generated by Django 3.0.6 on 2020-05-16 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200516_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Bekliyor', 'Bekliyor'), ('Teslim Edildi', 'Teslim Edildi')], max_length=200, null=True),
        ),
    ]
