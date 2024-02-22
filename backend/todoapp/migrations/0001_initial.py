# Generated by Django 4.2.10 on 2024-02-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=500)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
