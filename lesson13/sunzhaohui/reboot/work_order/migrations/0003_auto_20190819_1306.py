# Generated by Django 2.2 on 2019-08-19 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_order', '0002_auto_20190819_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='status',
            field=models.IntegerField(choices=[(0, '申请'), (1, '处理中'), (2, '完成'), (3, '失败'), (4, '已取消')], default=0, verbose_name='工单状态'),
        ),
    ]
