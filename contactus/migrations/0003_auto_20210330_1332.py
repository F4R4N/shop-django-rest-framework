# Generated by Django 3.1.5 on 2021-03-30 17:32

import contactus.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0002_auto_20210328_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='MassEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=contactus.utils.random_key, max_length=13, unique=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('admin_name', models.CharField(blank=True, max_length=30, null=True)),
                ('subject', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='key',
            field=models.CharField(default=contactus.utils.random_key, max_length=13, unique=True),
        ),
    ]
