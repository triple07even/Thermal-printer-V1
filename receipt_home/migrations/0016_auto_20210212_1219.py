# Generated by Django 3.1.5 on 2021-02-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_home', '0015_auto_20210212_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='created_on',
            field=models.DateTimeField(),
        ),
    ]
