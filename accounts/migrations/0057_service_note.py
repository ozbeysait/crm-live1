# Generated by Django 3.0.6 on 2020-07-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0056_auto_20200730_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]