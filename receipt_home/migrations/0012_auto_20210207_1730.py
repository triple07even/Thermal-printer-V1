# Generated by Django 3.1.5 on 2021-02-07 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_home', '0011_drug_drug_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='drug_test',
            field=models.CharField(max_length=10),
        ),
    ]
