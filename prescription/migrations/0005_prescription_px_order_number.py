# Generated by Django 3.2.24 on 2024-05-01 20:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0004_auto_20240428_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='px_order_number',
            field=models.CharField(default=django.utils.timezone.now, editable=False, max_length=32),
            preserve_default=False,
        ),
    ]
