# Generated by Django 5.0.6 on 2024-05-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_yourmodel_delete_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourmodel',
            name='pho',
            field=models.BigIntegerField(),
        ),
    ]
