# Generated by Django 3.2.24 on 2024-04-27 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='px_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]