# Generated by Django 3.1.3 on 2022-03-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_photo_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
