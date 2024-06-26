# Generated by Django 3.2.24 on 2024-04-13 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_communicationcontent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='communicationcontent',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Communication Content'},
        ),
        migrations.AddField(
            model_name='communicationcontent',
            name='content_type',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to='home.communicationtype'),
        ),
    ]
