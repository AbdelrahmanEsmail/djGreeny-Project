# Generated by Django 3.2 on 2022-09-06 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_brand_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category/', verbose_name='Image'),
        ),
    ]
