# Generated by Django 3.2.3 on 2022-06-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_auto_20220527_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tot_cost',
            field=models.DecimalField(decimal_places=2, default=120.0, max_digits=6),
            preserve_default=False,
        ),
    ]
