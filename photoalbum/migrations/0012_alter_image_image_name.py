# Generated by Django 3.2.8 on 2021-10-18 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoalbum', '0011_alter_image_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_name',
            field=models.FileField(upload_to='photoalbum/image/'),
        ),
    ]
