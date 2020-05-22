# Generated by Django 2.2.3 on 2020-04-17 10:04

import dashboard.mixins.draftables
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0027_allow_blanks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_title', models.CharField(max_length=50)),
                ('credit_title_order', models.IntegerField(default=0)),
                ('credit_user_name', models.CharField(max_length=50)),
                ('is_user', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'article_credit',
                'ordering': ['credit_title_order'],
            },
        ),
        migrations.AlterModelOptions(
            name='answercredit',
            options={'ordering': ['credit_title_order']},
        ),
        migrations.AlterField(
            model_name='answercredit',
            name='user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='answer_credits', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answertranslation',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('hi', 'हिंदी')], default='en', max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('hi', 'हिंदी')], default='en', max_length=100),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('hi', 'हिंदी')], default='en', max_length=100),
        ),
        migrations.AlterField(
            model_name='translatedquestion',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('hi', 'हिंदी')], default='en', max_length=100),
        ),
        migrations.DeleteModel(
            name='AnswerComment',
        ),
        migrations.AddField(
            model_name='articlecredit',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='dashboard.Article'),
        ),
        migrations.AddField(
            model_name='articlecredit',
            name='user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='article_credits', to=settings.AUTH_USER_MODEL),
        ),
    ]
