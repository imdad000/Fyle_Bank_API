# Generated by Django 2.2.3 on 2019-07-18 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fyleApp', '0005_auto_20190718_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branches',
            old_name='ifsc_code',
            new_name='ifsc',
        ),
    ]
