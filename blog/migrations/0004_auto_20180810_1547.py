# Generated by Django 2.0.7 on 2018-08-10 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180810_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
