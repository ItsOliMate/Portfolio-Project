# Generated by Django 3.0.8 on 2020-07-24 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20200724_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='About',
            new_name='about',
        ),
    ]
