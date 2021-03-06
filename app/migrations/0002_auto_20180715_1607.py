# Generated by Django 2.0.7 on 2018-07-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mono', models.CharField(max_length=13)),
                ('used_email', models.CharField(max_length=30)),
                ('msg', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.RemoveField(
            model_name='car',
            name='Images',
        ),
        migrations.AlterField(
            model_name='car',
            name='Currentl_Available',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='Year_discontinued',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='car',
            name='Year_introduced',
            field=models.CharField(max_length=5),
        ),
    ]
