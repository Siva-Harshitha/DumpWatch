# Generated by Django 5.1.6 on 2025-02-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('complaint', models.TextField()),
                ('marked', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='complaints/')),
            ],
        ),
    ]
