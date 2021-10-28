# Generated by Django 4.0b1 on 2021-10-28 08:43

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avator',
            field=models.ImageField(default='default-avator.jpg', upload_to=accounts.models.get_avator_path),
        ),
    ]
