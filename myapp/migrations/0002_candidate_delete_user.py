# Generated by Django 5.0.6 on 2024-05-21 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.CharField(max_length=100, unique=True)),
                ('certificate_file', models.FileField(upload_to='certificates/')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]