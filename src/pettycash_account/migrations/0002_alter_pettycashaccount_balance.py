# Generated by Django 4.1.5 on 2023-01-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pettycash_account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pettycashaccount',
            name='balance',
            field=models.IntegerField(),
        ),
    ]