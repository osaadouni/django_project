# Generated by Django 2.1.8 on 2019-04-02 10:30

from django.db import migrations, models
import simple_upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to=simple_upload.models.user_directory_path)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/%Y/%m/%d/'),
        ),
    ]
