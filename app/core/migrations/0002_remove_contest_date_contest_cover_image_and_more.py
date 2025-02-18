# Generated by Django 4.0.8 on 2022-10-21 03:03

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='date',
        ),
        migrations.AddField(
            model_name='contest',
            name='cover_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='封面圖片'),
        ),
        migrations.AddField(
            model_name='contest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='建立時間'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contest',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=255, verbose_name='聯絡信箱'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contest',
            name='end_at',
            field=models.DateField(blank=True, null=True, verbose_name='結束於'),
        ),
        migrations.AddField(
            model_name='contest',
            name='identity_restrictions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None, verbose_name='身份限制'),
        ),
        migrations.AddField(
            model_name='contest',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contest',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contest',
            name='regional_restrictions',
            field=django_countries.fields.CountryField(default='TW', max_length=2, verbose_name='國家/地區限制'),
        ),
        migrations.AddField(
            model_name='contest',
            name='saved',
            field=models.ManyToManyField(blank=True, related_name='saved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contest',
            name='start_from',
            field=models.DateField(blank=True, null=True, verbose_name='開始於'),
        ),
        migrations.AddField(
            model_name='contest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新時間'),
        ),
        migrations.AddField(
            model_name='contest',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='contest',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='', verbose_name='圖片'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='連結'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='比賽名稱'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='organizer',
            field=models.CharField(max_length=255, null=True, verbose_name='主辦單位'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None, verbose_name='標籤'),
        ),
    ]
