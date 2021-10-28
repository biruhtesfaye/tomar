# Generated by Django 4.0b1 on 2021-10-27 15:05

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(help_text='Select an eye catching image to be used as a cover photo for your post. This will attract users to read your post.', upload_to=blog.models.get_image_path),
        ),
    ]