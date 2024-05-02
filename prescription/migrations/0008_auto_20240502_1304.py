# Generated by Django 3.2.24 on 2024-05-02 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_rename_default_user_userprofile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prescription', '0007_auto_20240502_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='px_orders', to='profiles.userprofile'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prescription_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
