# Generated by Django 2.2.3 on 2020-03-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_website', '0003_auto_20200328_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactussubmission',
            name='message',
            field=models.TextField(max_length=200),
        ),
    ]
