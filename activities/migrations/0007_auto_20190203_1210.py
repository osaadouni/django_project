# Generated by Django 2.1.3 on 2019-02-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_auto_20190203_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='charge_per_hour',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='charge per hour:'),
        ),
    ]