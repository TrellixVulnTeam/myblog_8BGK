# Generated by Django 2.2 on 2021-12-04 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20211204_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articletopic',
            old_name='topic',
            new_name='t_name',
        ),
    ]
