# Generated by Django 4.0.1 on 2022-02-14 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import photo.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='NAME')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='One Line Description')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(default=0, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='상품 제목')),
                ('money', models.CharField(max_length=10, verbose_name='상품 가격')),
                ('season', models.CharField(max_length=20, verbose_name='상품 시즌')),
                ('style', models.TextField(blank=True, verbose_name='스타일')),
                ('size', models.TextField(blank=True, verbose_name='사이즈')),
                ('Material', models.TextField(blank=True, verbose_name='소재')),
                ('image', photo.fields.ThumbnailImageField(upload_to='photo/%Y/%m', verbose_name='상품 사진')),
                ('upload_dt', models.DateTimeField(auto_now_add=True, verbose_name='UPLOAD DATE')),
                ('stock', models.IntegerField(verbose_name='재고 수량')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.album')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
