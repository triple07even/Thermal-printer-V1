# Generated by Django 3.1.5 on 2021-01-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_home', '0003_auto_20210118_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='desc',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
