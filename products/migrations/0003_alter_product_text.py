# Generated by Django 4.0.4 on 2022-05-22 11:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
