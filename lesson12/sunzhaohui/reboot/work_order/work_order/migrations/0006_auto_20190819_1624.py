# Generated by Django 2.2 on 2019-08-19 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_order', '0005_auto_20190819_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='complete_time',
            field=models.DateTimeField(verbose_name='处理完成时间'),
        ),
        migrations.AlterField(
            model_name='workorder',
            name='handle_time',
            field=models.DateTimeField(verbose_name='处理时间'),
        ),
    ]