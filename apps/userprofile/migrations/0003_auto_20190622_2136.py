# Generated by Django 2.2.1 on 2019-06-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20190529_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default=0, max_length=128, verbose_name='密码'),
            preserve_default=False,
        ),
    ]