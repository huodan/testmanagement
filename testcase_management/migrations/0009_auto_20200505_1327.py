# Generated by Django 3.0.5 on 2020-05-05 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testcase_management', '0008_auto_20200505_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcase',
            old_name='tid',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='testplan',
            old_name='pid',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='testcastrunlog',
            name='testcase_id',
            field=models.ForeignKey(db_column='testcase_id', on_delete=django.db.models.deletion.CASCADE, to='testcase_management.Testcase'),
        ),
        migrations.AlterField(
            model_name='testcastrunlog',
            name='testplan_id',
            field=models.ForeignKey(db_column='testplan_id', on_delete=django.db.models.deletion.CASCADE, to='testcase_management.Testplan'),
        ),
        migrations.AlterField(
            model_name='testplan',
            name='testcase_id',
            field=models.ForeignKey(db_column='testcase_id', on_delete=django.db.models.deletion.CASCADE, to='testcase_management.Testcase'),
        ),
    ]
