# Generated by Django 4.0.2 on 2022-04-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_on',
            field=models.DateTimeField(blank=True),
        ),
    ]
