# Generated by Django 2.1.3 on 2019-01-14 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='activity',
            name='charge_per_hour',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='charge per hour:'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='name',
            field=models.CharField(max_length=50, verbose_name='activity name:'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='skill_level',
            field=models.CharField(choices=[('', '-- (Select level)--'), ('low', 'Low'), ('high', 'High'), ('inter', 'Intermediate')], default='', max_length=10, verbose_name='skill level:'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='sold_per_hour',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, verbose_name='sold per hour:'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='vat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, verbose_name='vat:'),
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.Category', verbose_name='category'),
        ),
    ]
