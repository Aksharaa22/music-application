# Generated by Django 3.2.3 on 2022-04-25 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('channel_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10000)),
                ('music', models.CharField(max_length=100000)),
            ],
        ),
    ]