# Generated by Django 2.0.7 on 2018-07-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180715_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='model_pic',
            field=models.ImageField(default='static/no-img.jpg', upload_to='static'),
        ),
    ]
