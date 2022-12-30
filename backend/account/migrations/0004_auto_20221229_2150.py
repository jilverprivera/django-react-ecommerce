# Generated by Django 3.2.7 on 2022-12-30 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20221221_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='thumbnail',
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='user/uploads/default_image.jpeg', null=True, upload_to='user/uploads/'),
        ),
    ]
