# Generated by Django 4.2.4 on 2023-09-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0035_contract_end_date_contract_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='years',
            field=models.IntegerField(null=True),
        ),
    ]
