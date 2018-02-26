# Generated by Django 2.0.1 on 2018-02-26 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='watchshop_logo/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='watchshop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
