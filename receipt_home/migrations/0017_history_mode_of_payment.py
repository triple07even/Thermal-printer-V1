# Generated by Django 3.1.5 on 2021-02-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_home', '0016_auto_20210212_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='mode_of_payment',
            field=models.CharField(default=None, max_length=5),
            preserve_default=False,
        ),
    ]