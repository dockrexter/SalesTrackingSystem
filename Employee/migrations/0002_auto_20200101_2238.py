# Generated by Django 3.0.1 on 2020-01-01 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Products'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Zones'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Products'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Zones'),
        ),
        migrations.AlterField(
            model_name='stockmanager',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.Products'),
        ),
    ]