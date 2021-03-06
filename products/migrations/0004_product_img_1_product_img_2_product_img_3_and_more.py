# Generated by Django 4.0.4 on 2022-05-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img_1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='img_2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='img_3',
            field=models.ImageField(default='dwa', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='main_img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
