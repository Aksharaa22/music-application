# Generated by Django 3.2.3 on 2022-05-16 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_shproduct_shcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shcart',
            name='shproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shproduct', verbose_name='Product'),
        ),
    ]