# Generated by Django 4.2.4 on 2023-08-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Your_Name', models.CharField(max_length=50)),
                ('Your_Email', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
    ]
