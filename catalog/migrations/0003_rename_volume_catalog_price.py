# Generated by Django 3.2.3 on 2021-12-16 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20211216_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalog',
            old_name='volume',
            new_name='price',
        ),
    ]