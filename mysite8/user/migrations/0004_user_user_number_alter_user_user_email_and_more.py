# Generated by Django 4.0.1 on 2022-02-11 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_number',
            field=models.CharField(default=1, max_length=20, unique=True, verbose_name='휴대전화'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(max_length=128, unique=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(max_length=32, unique=True, verbose_name='아이디'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=16, unique=True, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_pw',
            field=models.CharField(max_length=128, verbose_name='비밀번호'),
        ),
    ]
