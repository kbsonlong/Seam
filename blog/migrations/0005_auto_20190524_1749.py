# Generated by Django 2.2.1 on 2019-05-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190524_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(auto_created=True, blank=True, verbose_name='发布时间'),
        ),
    ]
