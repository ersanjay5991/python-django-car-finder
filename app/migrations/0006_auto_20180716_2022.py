# Generated by Django 2.0.7 on 2018-07-16 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180716_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Long_Model',
            field=models.CharField(max_length=50),
        ),
    ]
