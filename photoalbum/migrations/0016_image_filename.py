# Generated by Django 3.2.8 on 2021-10-18 13:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0015_alter_image_image_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='filename',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
