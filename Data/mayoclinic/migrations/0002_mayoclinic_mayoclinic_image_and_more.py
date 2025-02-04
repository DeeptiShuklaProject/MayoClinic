# Generated by Django 5.0.6 on 2024-07-03 14:15

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayoclinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mayoclinic',
            name='mayoclinic_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='mayoclinic/'),
        ),
        migrations.AddField(
            model_name='mayoclinic',
            name='mayoclinic_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='mayoclinic_title', unique=True),
        ),
    ]
