# Generated by Django 3.1 on 2020-09-01 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spacerentals', '0004_auto_20200826_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='dob',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='booking',
            name='timeperiod',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.CharField(max_length=10)),
                ('desc', models.TextField()),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
