# Generated by Django 4.2.4 on 2023-08-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(default='https://img.freepik.com/free-icon/man_318-677829.jpg', null=True, upload_to='pics'),
        ),
    ]