# Generated by Django 4.2.9 on 2024-02-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(blank=True, upload_to='pictures/image/%Y/%m/%d'),
        ),
    ]
