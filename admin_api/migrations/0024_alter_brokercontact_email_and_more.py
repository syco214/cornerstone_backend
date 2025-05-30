# Generated by Django 5.1.3 on 2025-05-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0023_inventory_pattern'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokercontact',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='brokercontact',
            name='office_number',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='brokercontact',
            name='personal_number',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='forwardercontact',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='forwardercontact',
            name='office_number',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='forwardercontact',
            name='personal_number',
            field=models.TextField(),
        ),
    ]
