# Generated by Django 2.2.3 on 2020-02-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sawaliram_auth', '0016_auto_20200208_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password_reset_code',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='password_reset_code_expiry',
            field=models.DateTimeField(null=True),
        ),
    ]
