# Generated by Django 4.2.4 on 2024-02-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0051_tour_cancelled'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='edited',
            field=models.BooleanField(default=False),
        ),
    ]