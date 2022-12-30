# Generated by Django 3.2.7 on 2022-12-30 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20221229_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128)),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
                'ordering': ('created_at',),
            },
        ),
    ]
