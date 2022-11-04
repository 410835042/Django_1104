# Generated by Django 3.2.9 on 2022-09-02 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20220902_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='src/media/image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='threeD_model',
            field=models.FileField(blank=True, null=True, upload_to='src/media/gltf/'),
        ),
    ]