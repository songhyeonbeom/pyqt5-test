# Generated by Django 3.1.3 on 2022-02-02 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import photo.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='money',
            field=models.CharField(default=1, max_length=10, verbose_name='상품 가격'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, verbose_name='상세설명'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=photo.fields.ThumbnailImageField(upload_to='photo/%Y/%m', verbose_name='상품 사진'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=30, verbose_name='상품 제목'),
        ),
    ]