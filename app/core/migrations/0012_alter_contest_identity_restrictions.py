# Generated by Django 4.0.8 on 2022-10-30 14:21

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_contest_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='identity_restrictions',
            field=core.models.ChoiceArrayField(base_field=models.CharField(blank=True, choices=[('junior', '高中組'), ('personal', '個人組'), ('team', '團體組'), ('fingerstyle', '演奏組'), ('society', '社會組')], default='personal', max_length=12, null=True), size=None, verbose_name='身份限制'),
        ),
    ]
