# Generated by Django 3.0.6 on 2020-08-12 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0063_auto_20200811_1639'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date_created',
            new_name='dateCreated',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='email_durumu',
            new_name='emailStatu',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='product_key',
            new_name='fax',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='tax_admin',
            new_name='gsm',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='bakim_anlasmasi',
            new_name='maintenance',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='bakim_baslangic',
            new_name='maintenanceEndDate',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='bakim_bitis',
            new_name='maintenanceStartDate',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='tax_number',
            new_name='productKey',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_customer',
            new_name='serviceCustomer',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_date',
            new_name='serviceDate',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='service_name',
            new_name='serviceName',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='solution_name',
            new_name='solutionName',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='create_at',
            new_name='createAt',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='update_at',
            new_name='updateAt',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='todo_date',
            new_name='todoDate',
        ),
        migrations.AddField(
            model_name='customer',
            name='adress',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='productClient',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='productName',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='taxAdmin',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='taxNumber',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='town',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='rate',
            field=models.CharField(blank=True, choices=[('Çok Kötü', 'Çok Kötü'), ('Kötü', 'Kötü'), ('Orta', 'Orta'), ('İyi', 'İyi'), ('Çok İyi', 'Çok İyi'), ('Mükemmel', 'Mükemmel')], max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Yeni', 'Yeni'), ('Kapalı', 'Kapalı')], default='Yeni', max_length=10),
        ),
    ]
