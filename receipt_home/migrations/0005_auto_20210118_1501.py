# Generated by Django 3.1.5 on 2021-01-18 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_home', '0004_drug_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='amount',
            new_name='ammount',
        ),
    ]
