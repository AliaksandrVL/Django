# Generated by Django 2.0.7 on 2018-07-17 10:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('publicated', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
            ],
        ),
    ]
