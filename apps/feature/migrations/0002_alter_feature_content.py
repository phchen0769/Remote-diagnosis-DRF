# Generated by Django 5.1.2 on 2024-11-29 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='content',
            field=models.CharField(help_text='内容', max_length=2000, null=True, verbose_name='内容'),
        ),
    ]
