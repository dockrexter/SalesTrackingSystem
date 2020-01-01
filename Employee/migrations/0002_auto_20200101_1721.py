# Generated by Django 3.0.1 on 2020-01-01 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Zones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StockManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Employee.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('retailer', models.CharField(max_length=300)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Employee.Products')),
                ('zone', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Employee.Zones')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='zone',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Employee.Zones'),
        ),
    ]
