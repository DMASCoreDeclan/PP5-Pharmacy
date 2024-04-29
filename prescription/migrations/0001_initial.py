# Generated by Django 3.2.24 on 2024-04-24 15:33

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
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('date_required', models.DateTimeField(auto_now=True)),
                ('dr_full_name', models.CharField(max_length=50)),
                ('px_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('px_status', models.CharField(choices=[('0', 'To be Processed'), ('1', 'Being Processed'), ('2', 'Processed'), ('3', 'Cannot be Processed')], default=0, max_length=20)),
                ('px_delivery', models.CharField(choices=[('0', 'Being Collected'), ('1', 'Being Delivered')], default=0, max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prescription_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]