# Generated by Django 5.0.2 on 2024-02-24 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_remove_menu_parent_menu_remove_menu_url_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='children',
        ),
        migrations.AddField(
            model_name='menu',
            name='parent_menu',
            field=models.ForeignKey(blank=True, help_text='父菜单', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_menu', to='user.menu', verbose_name='父类菜单'),
        ),
    ]
