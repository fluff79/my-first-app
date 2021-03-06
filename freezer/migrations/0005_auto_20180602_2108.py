# Generated by Django 2.0.4 on 2018-06-02 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freezer', '0004_shopping_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='on_shopping_list',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='where',
            field=models.IntegerField(choices=[(1, 'Kitchen: Top tray'), (2, 'Kitchen: Middle drawer'), (3, 'Kitchen: Bottom drawer'), (4, 'Utility: Top tray'), (5, 'Utility: 1st drawer'), (6, 'Utility: 2nd drawer'), (7, 'Utility: 3rd drawer'), (8, 'Utility: 4th drawer'), (9, 'Utility: 5th drawer'), (10, 'None')], default=1),
        ),
    ]
