# Generated by Django 3.1.3 on 2022-03-24 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import insta.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='NAME')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='One Line Description')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='TITLE')),
                ('description', models.TextField(blank=True, verbose_name='Photo Description')),
                ('image', insta.fields.ThumbnailImageField(upload_to='insta/%Y/%m', verbose_name='IMAGE')),
                ('upload_dt', models.DateTimeField(auto_now_add=True, verbose_name='UPLOAD DATE')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.album')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_photo', to=settings.AUTH_USER_MODEL)),
                ('voter', models.ManyToManyField(related_name='voter_photo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.photo')),
            ],
        ),
    ]
