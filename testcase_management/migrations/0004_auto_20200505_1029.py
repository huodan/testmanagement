# Generated by Django 3.0.5 on 2020-05-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcase_management', '0003_auto_20200505_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='create_time',
            field=models.IntegerField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='update_time',
            field=models.IntegerField(verbose_name='更新时间'),
        ),
    ]
