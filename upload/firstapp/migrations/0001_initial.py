# Generated by Django 3.1.4 on 2020-12-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diamond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.TextField(max_length=60)),
                ('cut', models.TextField(max_length=60)),
                ('clarity', models.TextField(max_length=60)),
                ('caratWeight', models.FloatField(max_length=60)),
            ],
        ),
    ]
