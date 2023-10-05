# Generated by Django 4.2.4 on 2023-10-04 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0036_contract_years'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wage', models.IntegerField()),
                ('fees', models.IntegerField()),
                ('bonus', models.CharField(max_length=200)),
                ('contractAccepted', models.BooleanField(default=False)),
                ('player_negotiating', models.BooleanField(default=False)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('years', models.IntegerField(null=True)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_as_club', to=settings.AUTH_USER_MODEL)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_as_player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]