# Generated by Django 3.2.9 on 2022-10-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ring_size', models.CharField(max_length=10)),
                ('centimeter', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
