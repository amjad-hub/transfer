# Generated by Django 3.2.6 on 2021-08-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_To_TIN', models.CharField(max_length=400)),
                ('amount_money', models.DecimalField(decimal_places=1, max_digits=100)),
            ],
        ),
    ]
