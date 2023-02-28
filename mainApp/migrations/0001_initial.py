# Generated by Django 4.1.5 on 2023-02-28 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200)),
                ('email', models.EmailField(default=None, max_length=30)),
                ('phone_number', models.CharField(max_length=255)),
                ('password', models.CharField(default=None, max_length=10, null=True)),
            ],
        ),
    ]
