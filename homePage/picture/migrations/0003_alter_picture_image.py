# Generated by Django 4.2.9 on 2024-02-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0002_alter_picture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='pictures/image/%Y/%m/%d'),
        ),
    ]
