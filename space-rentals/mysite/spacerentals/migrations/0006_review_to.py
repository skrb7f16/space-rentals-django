# Generated by Django 3.1 on 2020-09-01 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacerentals', '0005_auto_20200902_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='to',
            field=models.IntegerField(default=1),
        ),
    ]