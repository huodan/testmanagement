# Generated by Django 3.0.5 on 2020-05-05 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testcase_management', '0005_auto_20200505_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcastrunlog',
            old_name='case_id',
            new_name='testcase',
        ),
        migrations.RenameField(
            model_name='testcastrunlog',
            old_name='plan_id',
            new_name='testplan',
        ),
        migrations.AlterField(
            model_name='testcase',
            name='module',
            field=models.CharField(default='transaction', max_length=80, verbose_name='模块名'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='priority',
            field=models.IntegerField(default=0, verbose_name='优先级'),
        ),
    ]