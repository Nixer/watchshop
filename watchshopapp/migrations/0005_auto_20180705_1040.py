# Generated by Django 2.0.1 on 2018-07-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchshopapp', '0004_auto_20180705_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchshop',
            name='logo',
            field=models.ImageField(blank=True, upload_to='watchshop_logo/'),
        ),
    ]