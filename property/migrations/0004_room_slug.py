# Generated by Django 3.1.3 on 2020-11-27 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20201127_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
