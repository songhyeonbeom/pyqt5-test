# Generated by Django 4.0 on 2022-01-03 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]