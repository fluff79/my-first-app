# Generated by Django 2.0.4 on 2018-05-09 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freezer', '0002_auto_20180509_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='item',
            name='text',
        ),
    ]
