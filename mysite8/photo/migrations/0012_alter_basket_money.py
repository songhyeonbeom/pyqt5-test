# Generated by Django 4.0.1 on 2022-02-14 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0011_remove_basket_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='money',
            field=models.IntegerField(default=0, max_length=250),
        ),
    ]
