# Generated by Django 3.1 on 2020-08-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacerentals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pg',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
