# Generated by Django 3.2.3 on 2022-04-25 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_channel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prtitle', models.CharField(max_length=50, verbose_name='Category Title')),
                ('prslug', models.SlugField(max_length=55, verbose_name='Category Slug')),
                ('prdescription', models.TextField(blank=True, verbose_name='Category Description')),
                ('prcategory_image', models.ImageField(blank=True, null=True, upload_to='category', verbose_name='Category Image')),
                ('pris_active', models.BooleanField(verbose_name='Is Active?')),
                ('pris_featured', models.BooleanField(verbose_name='Is Featured?')),
                ('prcreated_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('prupdated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
            ],
            options={
                'verbose_name_plural': 'PrCategories',
                'ordering': ('-prcreated_at',),
            },
        ),
        migrations.CreateModel(
            name='PrProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prtitle', models.CharField(max_length=150, verbose_name='Product Title')),
                ('prslug', models.SlugField(max_length=160, verbose_name='Product Slug')),
                ('prsku', models.CharField(max_length=255, unique=True, verbose_name='Unique Product ID (SKU)')),
                ('prshort_description', models.TextField(verbose_name='Short Description')),
                ('prdetail_description', models.TextField(blank=True, null=True, verbose_name='Detail Description')),
                ('prproduct_image', models.ImageField(blank=True, null=True, upload_to='product', verbose_name='Product Image')),
                ('prprice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('prsong', models.FileField(upload_to='product')),
                ('pris_active', models.BooleanField(verbose_name='Is Active?')),
                ('pris_featured', models.BooleanField(verbose_name='Is Featured?')),
                ('prcreated_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('prupdated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('prcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='Product Categoy')),
            ],
            options={
                'verbose_name_plural': 'PrProducts',
                'ordering': ('-prcreated_at',),
            },
        ),
    ]
