# Generated by Django 2.1.3 on 2019-02-02 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
        ('activities', '0003_auto_20190114_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='departments',
            field=models.ManyToManyField(blank=True, null=True, to='departments.Department'),
        ),
    ]
