# Generated by Django 4.2.4 on 2023-08-29 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myselfapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='Message',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='Subject',
            field=models.CharField(max_length=255),
        ),
    ]
