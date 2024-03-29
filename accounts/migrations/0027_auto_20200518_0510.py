# Generated by Django 3.0.6 on 2020-05-18 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20200518_0508'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bakim_anlasmasi',
            field=models.CharField(choices=[('Aktif', 'Aktif'), ('Pasif', 'Pasif')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='bakim_baslangic',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='bakim_bitis',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pruduct_key',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='tax_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
