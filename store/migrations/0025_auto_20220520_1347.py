# Generated by Django 3.2.3 on 2022-05-20 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_auto_20220520_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msproduct',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='msproducttwo',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]