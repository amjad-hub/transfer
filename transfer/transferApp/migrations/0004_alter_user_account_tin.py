# Generated by Django 3.2.6 on 2021-08-21 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferApp', '0003_transfer_transfer_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_account',
            name='TIN',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]
