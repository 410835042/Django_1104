# Generated by Django 3.2.9 on 2022-09-09 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0011_alter_account_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, '女'), (1, '男')], default=1, null=True),
        ),
    ]
