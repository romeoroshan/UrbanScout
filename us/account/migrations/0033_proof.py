# Generated by Django 4.2.4 on 2023-09-25 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0032_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=120, null=True)),
                ('payment_id', models.CharField(max_length=120, null=True)),
                ('signature', models.CharField(max_length=120, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proof_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
