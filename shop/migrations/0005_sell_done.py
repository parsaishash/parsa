# Generated by Django 3.1.2 on 2021-08-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_sell'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
