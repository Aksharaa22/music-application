# Generated by Django 3.2.3 on 2022-05-18 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0022_msproducttwo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='msproducttwo',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'MsProductstwo'},
        ),
        migrations.CreateModel(
            name='MsCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
